def convert_to_float(input_row):
    output_row = []
    for i in input_row:
        if("/" in i):
            split_res = i.split("/")
            floatable = float(split_res[0])/float(split_res[1])
            output_row.append(floatable)
        else:
            output_row.append(float(i))
    return output_row

print("Convert quadratic form to matrix:")
print("[x_1,x_2][[a,b],[c,d][[x_1],[x_2]]")
print("x^T*A*x")
print("Enter matrix comma separated 2 per row")
input_matrix_r1 = convert_to_float((input()).split(","))
input_matrix_r2 = convert_to_float((input()).split(","))
print("The form is: ",input_matrix_r1[0],"x_1^2 + ",2*input_matrix_r1[1],"x_1*x_2 + ",input_matrix_r2[1],"x_2^2")
while(True):
    print("Input your vector for eqn comma separated (vertical): or q to quit")
    vector_in = convert_to_float((input()).split(","))
    res_1 = input_matrix_r1[0]*(vector_in[0]*vector_in[0])
    res_2 = 2*input_matrix_r1[1]*(vector_in[0]*vector_in[1])
    res_3 = input_matrix_r2[1]*(vector_in[1]*vector_in[1])
    print("Result:",res_1," + ",res_2," + ",res_3)
    print("Total:",res_1+res_2+res_3)
    print("Done? q or Q  or enter to continue")
    qin = input()
    if('q' in qin or 'Q' in qin):
        break
