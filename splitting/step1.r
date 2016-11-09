to_date <- function (num) {
	EPOCH = '1970-01-01';
	return(as.POSIXct(num, EPOCH));
}

if (!exists('D', mode='list'))
	D <- read.csv('train.csv');

# Get customer ids & reverse index
cids = unique(D$ncodpers); # length is       956645 
inv_cids = vector(mode='numeric'); # max is 1553689
for (i in 1:length(cids)) {
	cid = cids[i];
	inv_cids[cid] = i;
}
print('defined cids and inv_cids');

# Vector of dates, where index corresponds to index of cids
months = vector(mode='list');
# How many CONTIGUOUS months does a each customer have?
counts = rep(0, length(cids));

# Iterate train.csv entries
for (i in 1:nrow(D)) {
	cid = D$ncodpers[i];
	mo  = to_date(D$fecha_dato[i]);
	idx = inv_cids[cid];
	if (is.na(idx)) stop('no index for cid in inv_cids: ', cid);
	if (length(months) < idx || is.null(months[[idx]]))
                months[[idx]] = vector(mode='numeric');
        months[[idx]] = append(mo, months[[idx]]);
	if (0 == i %% 10000) cat(sprintf('\titerated D row %d\n', i));
}
print('populated "months"');
save.image('Split.RData');


if (length(months) != length(cids))
	stop('mismatch len months vs cids: ', length(months), ':', length(cids));
if (sum(is.na(months)))
	stop('NA in months');
if (sum(is.na(cids)))
	stop('NA in cids');

# Count contiguous months for each customer
for (row_i in 1:length(months)) {
	pairs_ct = 0;
	mos = sort(months[[row_i]]);
	# Ensure there are no gaps in months
	if (length(mos) > 1) {
		for (i in 2:length(mos)) {
			delta = to_date(mos[i]) - to_date(mos[i-1]);
			if (abs(30 - delta) <= 3)
				pairs_ct = pairs_ct + 1;
		}
	}
	counts[row_i] = pairs_ct;
}
save.image('Split.RData');

df = data.frame(cids, counts);

save.image('Split.RData');

