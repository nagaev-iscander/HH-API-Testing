# утилита для запуска всех тестов

import subprocess

def run_test(test_name):
    print("Running " + test_name + "     ", end='')
    s = subprocess.check_output([test_name], shell=True, universal_newlines=True)
    print(s, end='')
   

print("Running autotests for https://api.hh.ru/vacancies/")

print("\n1) Simple general tests")
for i in range(4):
    test_name="test_1."+str(i+1)+".py"
    run_test(test_name)

print("\n2) Search expressions tests")
for i in range(7):
    test_name="test_2."+str(i+1)+".py"
    run_test(test_name)

print("\n3) Length tests")
for i in range(3):
    test_name="test_3."+str(i+1)+".py"
    run_test(test_name)
    
print("\n4) Test for binary data and special symbols")
for i in range(4):
    test_name="test_4."+str(i+1)+".py"
    run_test(test_name)
    
print("\n5) Logical expressions test")
test_name="test_5.1.py"
run_test(test_name)

print("\n6) Lewis Carroll words tests")
for i in range(2):
    test_name="test_6."+str(i+1)+".py"
    run_test(test_name)
