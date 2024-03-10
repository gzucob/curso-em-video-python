from utilityCeV import moeda
from utilityCeV import dados

valor = dados.leiamoney('Digite um valor: R$ ')
moeda.resumo(valor, 30, 15)
