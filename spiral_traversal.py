matrix = [
            [ 1 , 2 , 3 , 4 ] ,
            [ 5 , 6 , 7 , 8 ] ,
            [ 9 , 10 , 11 , 12 ] ,
            [ 13 , 14 , 15 , 16 ]
    ]
    
index1 = 0

while True :
            
    if index1 == 0 :
        
        for index2 in range ( 0 , len ( matrix [ index1 ] ) ) :
            print ( matrix [ index1 ] [ index2 ] )
        
        matrix .pop ( index1 )
        
        while index1 != len ( matrix ) - 1 :
            temp = len ( matrix [ index1 ] ) -1
            print ( matrix [ index1 ] [ temp ] )
            matrix [ index1 ] .pop ( temp )
            index1 += 1

        
    if index1 == len ( matrix ) - 1 :
        index2 = len ( matrix [ index1 ] ) - 1
        
        while matrix [ index1 ] :
            print ( matrix [ index1 ] [ index2 ] )
            matrix [ index1 ] .pop ( index2 )
            index2 -= 1
        
        matrix .pop ( index1 )
        index1 -= 1
        
        while index1 > -1 :
            print ( matrix [ index1 ] [ 0 ] )
            matrix [ index1 ] .pop ( 0 )
            index1 -= 1
        
        index1 = 0
        
    if len ( matrix ) == 0 : break

