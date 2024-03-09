def cat_and_mouse(x: int, y: int, z: int) -> str:
    if 0 < x <= 100 and 0 < y <= 100 and 0 < z <= 100 :
        distanceA_C = abs(z - x)
        distanceB_C = abs(z - y)
        if distanceA_C == distanceB_C:
            return 'Mouse C'
        if distanceA_C < distanceB_C :
            return 'Cat A'
        if distanceB_C < distanceA_C :
            return 'Cat B'
    else :
        return
