import math

def greedyEditdistance(X,Y):
        "Shifting strings to find maximum charecter overlap"
        #This functions assumes len(X) < len(Y) always, hence flipping if required
        flip = False
        if len(X) > len(Y):
            temp = X
            X = Y
            Y = temp
            flip = True

        
        opt_align_str1 = ""
        opt_align_str2 = ""
        min_edit_distance = math.inf
        #Shifting string Y, starting from X/2 last charecters concinciding with X/2 first charecters in string Y
        for shift_index in range(int(len(X)/2),-1,-1):
            str2 = shift_index*"-" + Y
            str1 = X + ( len(str2) - len(X) )*"-"
            count = 0
            for x, y in zip(str1, str2):
                if x != y:
                    count += 1
            if count < min_edit_distance:
                opt_align_str1 = str1
                opt_align_str2 = str2
                min_edit_distance = count
            
        #Shifting string X, first X/2 charecters coninciding with last X/2 charecters in string Y
        for shift_index in range(1,int(len(Y)-len(X)/2)+1):
            str1 = shift_index*"-" + X
            max_length = max (len(str1),len(Y))
            str2 = Y + "-"* (max_length - len(Y))
            str1 = str1 + "-"* (max_length - len(str1))

            count = 0
            for x, y in zip(str1, str2):
                if x != y:
                    count += 1
            if count < min_edit_distance:
                opt_align_str1 = str1
                opt_align_str2 = str2
                min_edit_distance = count

        if flip:
            return (opt_align_str2,opt_align_str1),min_edit_distance
        else:
            return (opt_align_str1,opt_align_str2),min_edit_distance


'''X = 'AGTACGCA'
Y = 'TATGC'
(align1,align2),ed = greedyEditdistance(X,Y)
print (align1,align2)
print (ed)

str1 = 'GCATGCU'
str2 = 'GATTACA'
(align1,align2),ed = greedyEditdistance(str1,str2)
print (align1,align2)
print (ed)
'''
