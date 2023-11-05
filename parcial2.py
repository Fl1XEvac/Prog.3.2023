def is_mutant(dna):
#Se hace un contador y si el contador es mayor a 0 se devolvera True
    count_dna_equals= 0
#Empiezas las verificaciones:

#Verificaciones horizontales
#Primer String
    for i in range(2):
        if dna[0][i] == dna[0][i+1] and dna[0][i+1] == dna[0][i+2] and dna[0][i+2] == dna[0][i+3]:
            count_dna_equals += 1
            break

#Segundo String
    for i in range(2):
        if dna[1][i] == dna[1][i+1] and dna[1][i+1] == dna[1][i+2] and dna[1][i+2] == dna[1][i+3]:
            count_dna_equals += 1
            break

#Tercer String
    for i in range(2):
        if dna[2][i] == dna[2][i+1] and dna[2][i+1] == dna[2][i+2] and dna[2][i+2] == dna[2][i+3]:
            count_dna_equals += 1
            break

#Cuarto String
    for i in range(2):
        if dna[3][i] == dna[3][i+1] and dna[3][i+1] == dna[3][i+2] and dna[3][i+2] == dna[3][i+3]:
            count_dna_equals += 1
            break

#Quinto String
    for i in range(2):
        if dna[4][i] == dna[4][i+1] and dna[4][i+1] == dna[4][i+2] and dna[4][i+2] == dna[4][i+3]:
            count_dna_equals += 1
            break

#Sexto String
    for i in range(2): 
        if dna[5][i] == dna[5][i+1] and dna[5][i+1] == dna[5][i+2] and dna[5][i+2] == dna[5][i+3]:
            count_dna_equals += 1
            break


#Verificaciones verticales

#Primera fila
    for i in range(2):
        if dna[i][0] == dna[i+1][0] and dna[i+1][0] == dna[i+2][0] and dna[i+2][0] == dna[i+3][0]:
            count_dna_equals += 1
            break

#Segunda fila
    for i in range(2):
        if dna[i][1] == dna[i+1][1] and dna[1][1] == dna[2][1] and dna[2][1] == dna[3][1]:
            count_dna_equals += 1
            break

#Tercer fila
    for i in range(2):
        if dna[i][2] == dna[i+1][2] and dna[1][2] == dna[2][2] and dna[2][2] == dna[3][2]:
            count_dna_equals += 1
            break

#Cuarta fila
    for i in range(2):
        if dna[i][3] == dna[i+1][3] and dna[1][3] == dna[2][3] and dna[2][3] == dna[3][3]:
            count_dna_equals += 1
            break

#Quinta fila
    for i in range(2):
        if dna[i][4] == dna[i+1][4] and dna[1][4] == dna[2][4] and dna[2][4] == dna[3][4]:
            count_dna_equals += 1
            break

#Sexta fila
    for i in range(2):
        if dna[i][5] == dna[i+1][5] and dna[1][5] == dna[2][5] and dna[2][5] == dna[3][5]:
            count_dna_equals += 1
            break

#Verificaciones diagonales

#Primera Diagonal
    for i in range(2):
        for j in range(2):
            if dna[i][j] == dna [i+1][j+1] and dna[i+1][j+1] == dna[i+2][j+2] and dna[i+2][j+2] == dna[i+3][i+3]:
                count_dna_equals +=1
                break

#Segunda Diagonal
    for i in range(1):
        for j in range(1):
            if dna[i+1][j] == dna [i+2][j+1] and dna[i+2][j+1] == dna[i+3][j+2] and dna[i+3][j+2] == dna[i+4][i+4]:
                count_dna_equals +=1
                break

#Tercer Diagonal
    if dna[2][0] == dna [3][1] and dna[3][1] == dna[4][2] and dna[4][2] == dna[5][3]:
        count_dna_equals +=1

#Diagonales desde 0:0 hasta 5:5, 1:0 hasta 5:4 y desde 2:0 hasta 5:3

#Cuarta Diagonal

    for i in range(1):
        for j in range(1):
            if dna[i][j+1] == dna [i+1][j+2] and dna[i+1][j+2] == dna[i+2][j+3] and dna[i+2][j+3] == dna[i+3][i+4]:
                count_dna_equals +=1
                break

#Quinta Diagonal
    if dna[0][2] == dna [1][3] and dna[1][3] == dna[2][4] and dna[2][4] == dna[3][5]:
        count_dna_equals +=1

#Diagonales desde 0:1 hasta 4:5 y desde 0:2 hasta 3:5

#Sexta Diagonal
    if dna[0][5] == dna[1][4] and dna[1][4] == dna [2][3] and dna[2][3] == dna[3][2]:
        count_dna_equals += 1
    elif dna[1][4] == dna[2][3] and dna[2][3] == dna[3][2] and dna[3][2] == dna[4][1]:
        count_dna_equals += 1

#Septima Diagonal
    if dna[0][4] == dna[1][3] and dna[1][3] == dna [2][2] and dna[2][2] == dna[4][1]:
        count_dna_equals += 1
    elif dna[1][3] == dna[2][2] and dna[2][2] == dna[3][1] and dna[3][1] == dna[4][0]:
        count_dna_equals += 1

#Octava Diagonal
    if dna[0][3] == dna[1][2] and dna[1][2] == dna[2][1] and dna[2][1] == dna[3][0]:
        count_dna_equals += 1

#Novena Diagonal
    if dna[1][5] == dna[2][4] and dna[2][4] == dna[3][3] and dna[3][3] == dna[4][2]:
        count_dna_equals += 1
    elif dna[2][4] == dna[3][3] and dna[3][3] == dna[4][2] and dna[4][2] == dna[5][1]:
        count_dna_equals += 1

#Decima Diagonal
    if dna[2][5] == dna[3][4] and dna[3][4] == dna[4][3] and dna[4][3] == dna[5][2]:
        count_dna_equals += 1

    if count_dna_equals > 1:
        return True


#Codigo principal:

valid_chars = set("ATCG")
max_attempts = 6
dna = []
# AGTTTT, TACTTA, CTATGG, ATTACC, TTCGAC, TAGCCT (MUTANTE)
# ATTCGG, GCAACC, ATTGGG, ACCTTT, CGGCAT, ATTGGC (NO MUTANTE)

#Se le pide al usuario el dna, y si ingresa otra letra que no sea A, T, C o G o si ingresa uno menor a 6, se le pide de nuevo
while len(dna) < max_attempts:
    sequence = input("Ingrese una secuencia de 6 letras para obtener el DNA del sujeto (A, T, C, G): ").upper()
    
    if all(char in valid_chars for char in sequence) and len(sequence) == 6:
        dna.append(sequence)
    else:
        print("Ha ingresado mal el DNA, porfavor, ingreselo de nuevo.")

#Verificacion si es mutante o no y llamada a la funcion is_mutant
result= is_mutant(dna)
if result == True:
    print("El sujeto es mutante")
else:
    print("El sujeto no es mutante")
