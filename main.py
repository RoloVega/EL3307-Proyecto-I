def main():
    cantidadVariables = 4
    minterminosUtilizados = [1,4,6,15]
    resultado = algoritmoQuineMcClusky(cantidadVariables, minterminosUtilizados)
    ecuacionSimplificada = resultado[0]
    tiempoEjecucion = resultado[1]
    #print(resultado)

def algoritmoQuineMcClusky(cantidadVariables, minterminosUtilizados):
    todosMinterminos = formarTodosMinterminos(cantidadVariables)
    
    #[[indiceMintermino], [valorBinarioMintermino], 0]
    minterminos = seleccionarMinterminos(todosMinterminos, minterminosUtilizados)

    #[[indicesMinterminos], [valorBinarioMintermino], cantidadUnos]
    minterminosAgrupadosCantidadUnos = agruparMinterminosCantidadUnos(minterminos, cantidadVariables)

    
    posibleCrearOtraTabla = verificarPosibleCrearOtraTabla(minterminosAgrupadosCantidadUnos)

    return [0,0]

def formarTodosMinterminos(cantidadVariables):
    valoresBinariosVariables = []
    minterminos = []
    for variable in range(0, cantidadVariables):
        valoresBinariosVariable = []
        cantidadGruposBinarios = 2**(variable+1)
        cantidadRepeticionesBinarias = (2**cantidadVariables)//cantidadGruposBinarios
        valorBinarioActual = "0"
        for grupoBinario in range(0, cantidadGruposBinarios):
            cantidadRepeticionesBinarias = (2**cantidadVariables)//cantidadGruposBinarios
            for repeticionBinaria in range(0, cantidadRepeticionesBinarias):
                valoresBinariosVariable = valoresBinariosVariable + [valorBinarioActual]
            if valorBinarioActual == "0":
                valorBinarioActual = "1"
            else:
                valorBinarioActual = "0"
        valoresBinariosVariables = valoresBinariosVariables + [valoresBinariosVariable]
    cantidadMinterminos = 2**cantidadVariables
    for indiceValoresBinariosVariables in range(0, cantidadMinterminos):
        mintermino = []
        for valoresBinariosVariable in valoresBinariosVariables:
            mintermino = mintermino + [valoresBinariosVariable[indiceValoresBinariosVariables]]
        minterminos = minterminos + [mintermino]
    return minterminos
        
def seleccionarMinterminos(todosMinterminos, minterminosUtilizados):
    minterminos = []
    cantidadMinterminos = len(todosMinterminos)
    for indiceMintermino in range(0, cantidadMinterminos):
        if indiceMintermino in minterminosUtilizados:
            minterminos = minterminos + [[[indiceMintermino],todosMinterminos[indiceMintermino],0]]
    return minterminos

def agruparMinterminosCantidadUnos(minterminos, cantidadVariables):
    minterminosAgrupadosCantidadUnos = []
    for posibleCantidadUnos in range(0, (cantidadVariables+1)):
        minterminosAgrupadosPosibleCantidadUnos = []
        for mintermino in minterminos:
            valorBinarioMintermino = mintermino[1]
            if valorBinarioMintermino.count("1") == posibleCantidadUnos:
                minterminosAgrupadosPosibleCantidadUnos = minterminosAgrupadosPosibleCantidadUnos + [[mintermino[0],mintermino[1],posibleCantidadUnos]]
        if minterminosAgrupadosPosibleCantidadUnos != []:
            minterminosAgrupadosCantidadUnos = minterminosAgrupadosCantidadUnos + [minterminosAgrupadosPosibleCantidadUnos]
    print(minterminosAgrupadosCantidadUnos)
    

def verificarPosibleCrearOtraTabla(minterminosAgrupadosCantidadUnos):
    pass


main()