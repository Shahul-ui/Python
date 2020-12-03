ages1 = {
    'ramesh':18,
    'mukesh':22,
    'syed':25
}
ages2 ={
    'basker':14,
    'abhishek':16
}
ages ={
    **ages1,
    **ages2
}
print(ages)
