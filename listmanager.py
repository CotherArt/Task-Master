# coding: utf-8
__author__ = 'CotherArt'

from task import Task
from pickle import dump, load as ld
from os import path
from pathlib import Path


class Listmanager:

    def __init__(self):
        self.listas = {}
        self.current_list = ''
        self.list_file = Path('listfile.tm')

        if path.exists(self.list_file):
            self.load()
        else:
            self.listas = {'TASKS': []}
            self.current_list = 'TASKS'
            self.save()

    #  Retorna True si la lista existe
    def list_exist(self, list_name):
        return list_name in self.listas.keys()

    #  Añade una nueva lista con el nombre de list_name
    def new_list(self, list_name):
        if self.list_exist(list_name):
            print("this list already exists")
            return
        self.listas[list_name] = []
        print('List "{}" added'.format(list_name))

    # Retorna la lista actual
    def get_current_list(self):
        if self.current_list == '':
            self.current_list = str(list(self.listas.keys())[0])
        return self.listas.get(self.current_list)

    # Selecciona una lista
    def set_current_list(self, list_name):
        if self.list_exist(list_name):
            self.current_list = list_name
        else:
            print('list name "{}" not found'.format(list_name))

    # Añade un item a la lista
    def add(self, msg):
        item = Task(msg)
        self.get_current_list().append(item)

    # Elimina un item de la lista
    def rm_task(self, msg):
        for i in self.get_current_list():
            if i.name == msg:
                self.get_current_list().remove(i)
                print('Element "{}" removed from "{}"'.format(i.name, self.current_list))
                return
        print('Item "{}" not found in "{}" list'.format(msg, self.current_list))

    # Elimina una lista
    def rm_list(self, list_name):
        yes_no = input("List {} will be removed [Yes/No]".format(list_name)).upper()
        print(yes_no)
        if yes_no != "YES":
            print("owo")
            return

        if list_name in self.listas.keys():
            del self.listas[list_name]
            print("List {} removed".format(list_name))
        else:
            print("List {} not found".format(list_name))

    # Imprime la lista
    def ls_tasks(self):
        if len(self.get_current_list()) == 0:
            print('List "{}" is empty'.format(self.current_list))
            return

        print('[{}]'.format(self.current_list))
        for i in self.get_current_list():
            print('-'*9)
            print('Name: {}\nChek: {}'.format(i.name, i.ischeck()))
        print('-'*9)

    # Imprime el nombre de todas las listas
    def ls_listas(self):
        print('[Listas]')
        for i in self.listas.keys():
            print('>', i)

    # Guarda la lista
    def save(self):
        with open(self.list_file, 'wb') as itemfile:
            dump(self.listas, itemfile)
            print('Lists saved')

    # Carga la lista desde el archivo
    def load(self):
        try:
            with open(self.list_file, 'rb') as itemfile:
                self.listas = ld(itemfile)
                print('Lists loaded from file')
        except:
            print('lists file do not exist')