import sqlite3
from pathlib import Path
import os
import time

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "cadastros.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row


def create_table(conn, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), cpf VARCHAR(11), cnpj VARCHAR(14))"
        )
    conn.commit()
#create_table(conn, cursor)


def register_cpf(conn, cursor, nome, cpf):
    data = (nome, cpf)
    cursor.execute("INSERT INTO clientes (nome, cpf) VALUES (?,?)", data)
    conn.commit()


def register_cnpj(conn, cursor, nome, cnpj):
    data = (nome, cnpj)
    cursor.execute("INSERT INTO clientes (nome, cnpj) VALUES (?,?)", data)
    conn.commit()


def update_client_cpf(conn, cursor, id, nome, cpf):
    data = (nome, cpf, id)
    cursor.execute("UPDATE clientes SET nome=?, cpf=? WHERE id=?", data)
    conn.commit()


def update_client_cnpj(conn, cursor, id, nome, cnpj):
    data = (nome, cnpj, id)
    cursor.execute("UPDATE clientes SET nome=?, cnpj=? WHERE id=?", data)
    conn.commit()


def show_physical_person(cursor):
    return cursor.execute("SELECT * FROM clientes WHERE cpf IS NOT NULL")


def show_juridical_person(cursor):
    return cursor.execute("SELECT * FROM clientes WHERE cnpj IS NOT NULL")


def for_physical_person():
    physical_person = show_physical_person(cursor)
    print('Physical person')
    for client in physical_person:
        print(f'Id: {client['id']} // Name: {client['nome']} // CPF: {client['cpf']}')


def for_juridical_person():
    juridical_person = show_juridical_person(cursor)
    print('Juridical person')
    for client in juridical_person:
        print(f'Id: {client['id']} // Name: {client['nome']} // CNPJ: {client['cnpj']}')


def delete_data_client(conn, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conn.commit()


def menu():
    while True:
        menu = input(
            '\n\t[1] Register physical person.'
            '\n\t[2] Register juridical person.'
            '\n\t[3] List registered physical persons.'
            '\n\t[4] List registered juridical persons.'
            '\n\t[5] Update physical person data.'
            '\n\t[6] Update juridical person data.'
            '\n\t[7] Delete data client.'
            '\n\t'
            '\n\t-> '
        )

        if menu == '1':
            nome = input("Inser client name: ")
            cpf = input('Insert client cpf: ')
            register_cpf(conn, cursor, nome, cpf)
            print('=== Successful register ===')
            time.sleep(2)
            os.system('cls')
        elif menu == '2':
            nome = input("Inser client name: ")
            cnpj = input('Insert client cnpj: ')
            register_cnpj(conn, cursor, nome, cnpj)
            print('=== Successful register ===')
            time.sleep(2)
            os.system('cls')
        elif menu == '3':
            for_physical_person()
            print('\n\t')
        elif menu == '4':
            for_juridical_person()
            print('\n\t')
        elif menu == '5':
            try:
                id = input('Insert id client: ')
                cursor.execute("SELECT * FROM clientes WHERE id=? AND cpf IS NOT NULL", (id,))
                client = cursor.fetchone()
                if client:
                    nome = input("Inser new client name: ")
                    cpf = input('Insert new client cpf: ')
                    if len(cpf) == 11:
                        update_client_cpf(conn, cursor, id, nome, cpf)
                        print('=== Update successful ===')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        print('Please, insert a valid cpf number.')
                else:
                    print("Physical person doesn't registered")
                    time.sleep(3)
                    os.system('cls')
            except Exception as exc:
                print(f'ERROR: {exc}')
                conn.rollback()
        elif menu == '6':
            try:
                id = input('Insert id client: ')
                cursor.execute("SELECT * FROM clientes WHERE id=? AND cnpj IS NOT NULL", (id,))
                client = cursor.fetchone()
                if client:
                    nome = input("Inser new client name: ")
                    cnpj = input('Insert new client cnpj: ')
                    if len(cnpj) == 14:
                        update_client_cnpj(conn, cursor, id, nome, cnpj)
                        print('=== Update successful ===')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        print('Please, insert a valid cnpj number.')
                else:
                    print("Juridical person doesn't registered")
                    time.sleep(3)
                    os.system('cls')
            except Exception as exc:
                print(f'ERROR: {exc}')
                conn.rollback()
        elif menu == '7':
            try:
                id = input('Insert client id: ')
                cursor.execute("SELECT id FROM clientes WHERE id=?", (id,))
                client = cursor.fetchone()
                if client:
                    delete_data_client(conn, cursor, id)
                    print('=== Successful Delete===')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print('Invalid ID.')
                    time.sleep(2)
                    os.system('cls')
            except Exception as exc:
                print(f'ERROR: {exc}')
                conn.rollback()


menu()