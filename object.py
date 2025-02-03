
conversion_object={
    "jan":"january",
    "feb":"february",
    "mar":"march"  
}
conversion_object['apr']='april'
print(conversion_object['feb'])
print(conversion_object.get('sdf', 'Not a valid key'))
print(conversion_object['apr'])