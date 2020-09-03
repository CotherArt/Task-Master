# coding: utf-8
__author__ = 'CotherArt'

from listhandler import Listhandler
import click

listhandler = Listhandler()


@click.command('--listname', help='Name of the list')
def hello(list_name):
    listhandler.ls_lists()

