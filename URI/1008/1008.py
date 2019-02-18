def main():
    funcionario = input()
    h_trab = input()
    vl_hora = input()
    sl_funcionario = int(h_trab) * float(vl_hora)
    print("NUMBER = {}".format(str(funcionario)))
    print("SALARY = U$ {0:.2f}".format(sl_funcionario))
main()
