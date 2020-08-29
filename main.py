# coding: utf-8
__author__ = 'CotherArt'

from item import Item
from pickle import dump, load as ld
from os import path
from pathlib import Path


class ToWatch:

    def __init__(self):
        self.listas = {}
        self.current_list = ''
        self.list_file = Path('listfile.list')

        if path.exists(self.list_file):
            self.load()
        else:
            self.listas = {'deflist': []}
            self.current_list = 'deflist'
            self.save()

    def new_list(self, list_name):
        self.listas[list_name] = []
        print('List "{}" added'.format(list_name))

    def get_current_list(self):
        if self.current_list == '':
            self.current_list = str(list(self.listas.keys())[0])
        return self.listas.get(self.current_list)

    def set_current_list(self, list_name):
        if list_name in self.listas:
            self.current_list = list_name
        else:
            print('list name "{}" not found'.format(list_name))

    def add(self, msg):  # Añade un item a la lista
        item = Item(msg)
        self.get_current_list().append(item)

    def rm(self, msg):  # elimina un item de la lista
        for i in self.get_current_list():
            if i.name == msg:
                self.get_current_list().remove(i)
                print('Element "{}" removed from "{}"'.format(i.name, self.current_list))
                pass
        print('Item "{}" not found in "{}" list'.format(msg, self.current_list))

    def ls(self):  # imprime la lista
        if len(self.get_current_list()) == 0:
            print('List "{}" is empty'.format(self.current_list))
            pass

        print('[{}]'.format(self.current_list))
        for i in self.get_current_list():
            print('--------------')
            print('Name: {}\nChek: {}'.format(i.name, i.ischeck()))
        print('--------------')

    def lst(self):  # Imprime el nombre de todas las listas
        print('[Listas]')
        for i in self.listas.keys():
            print('>', i)

    def save(self):  # Guarda la lista
        with open(self.list_file, 'wb') as itemfile:
            dump(self.listas, itemfile)
            print('Lists saved')

    def load(self):  # Carga la lista desde el archivo
        try:
            with open(self.list_file, 'rb') as itemfile:
                self.listas = ld(itemfile)
                print('Lists loaded from file')
        except:
            print('lists file do not exist')


if __name__ == '__main__':
    tw = ToWatch()
