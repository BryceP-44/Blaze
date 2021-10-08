#common maths

def nzmin(vector):
    for i in range(len(vector)):
        if vector[i]>2e-308:
            out=vector[i]
            break
    for i in range(len(vector)):
        if vector[i]<out and vector[i]>2e-308:
            out=vector[i]
    return out
