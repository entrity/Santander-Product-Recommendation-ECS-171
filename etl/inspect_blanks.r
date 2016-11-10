load('D.rda') # object containing all of train_ver2.csv

blanks.ind_empleado          = grep('^\\s*$', d$ind_empleado)
blanks.pais_residencia       = grep('^\\s*$', d$pais_residencia)
blanks.fecha_alta            = grep('^\\s*$', d$fecha_alta)
blanks.ind_nuevo             = grep('^\\s*$', d$ind_nuevo)
blanks.indrel                = grep('^\\s*$', d$indrel)
blanks.indresi               = grep('^\\s*$', d$indresi)
blanks.indext                = grep('^\\s*$', d$indext)
blanks.indfall               = grep('^\\s*$', d$indfall)
blanks.ind_actividad_cliente = grep('^\\s*$', d$ind_actividad_cliente)

print(sprintf('%d test %s', all(blanks.ind_empleado == blanks.pais_residencia), 'pais_residencia'))
print(sprintf('%d test %s', all(blanks.ind_empleado == blanks.fecha_alta), 'fecha_alta'))
print(sprintf('%d test %s', all(blanks.ind_empleado == blanks.ind_nuevo), 'ind_nuevo'))
print(sprintf('%d test %s', all(blanks.ind_empleado == blanks.indrel), 'indrel'))
print(sprintf('%d test %s', all(blanks.ind_empleado == blanks.indresi), 'indresi'))
print(sprintf('%d test %s', all(blanks.ind_empleado == blanks.indext), 'indext'))
print(sprintf('%d test %s', all(blanks.ind_empleado == blanks.indfall), 'indfall'))
print(sprintf('%d test %s', all(blanks.ind_empleado == blanks.ind_actividad_cliente), 'ind_actividad_cliente'))

if (!all(blanks.ind_empleado == blanks.pais_residencia))
    stop('mismatch 1')
if (!all(blanks.ind_empleado == blanks.fecha_alta))
    stop('mismatch 2')
if (!all(blanks.ind_empleado == blanks.ind_nuevo))
    stop('mismatch 3')
if (!all(blanks.ind_empleado == blanks.indrel))
    stop('mismatch 4')
if (!all(blanks.ind_empleado == blanks.indresi))
    stop('mismatch 5')
if (!all(blanks.ind_empleado == blanks.indext))
    stop('mismatch 6')
if (!all(blanks.ind_empleado == blanks.indfall))
    stop('mismatch 7')
if (!all(blanks.ind_empleado == blanks.ind_actividad_cliente))
    stop('mismatch 8')

# shorter_d = d[-blanks.ind_empleado,]

# It appears that all of the 9 columns which have exactly 27334 missing values
# are missing values on exactly the same rows, so I expect that it would be
# worthwhile to omit those rows.
