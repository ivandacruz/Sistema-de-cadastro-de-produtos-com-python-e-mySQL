from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()                                           # E só rodar o programa 
    linha2 = formulario.lineEdit_2.text()                                         # vai aparecer uma caixa de dialogo
    linha3 = formulario.lineEdit_3.text()
    
    if formulario.radioButton.isChecked():
        print("Categoria Informatica foi selecionado")
    elif formulario.radioButton_2.isChecked():
        print("Categoria Alimentos foi selecionado")  
    else:
        print("Categoria Eletronicos foi selecionado")   

    print("Codigo:",linha1)
    print("Descricao:",linha2)
    print("Preco:",linha3)



app = QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()