'''
Created on 28.11.2018

@author: mikaeltunturi
'''
from _hashlib import new
class Protozoan:
    
    NUMBER_OF_GENES = 10
    GENE_MIN_VALUE = 0
    GENE_MAX_VALUE = 5

    def __init__(self, given_name, genelist):
        self.__name = given_name
        a = 0
        list_of_genes = []
        for i in genelist:
            list_of_genes.append(i)
        for i in list_of_genes:
            if i < Protozoan.GENE_MIN_VALUE or i > Protozoan.GENE_MAX_VALUE:
                a += 1
        if a > 0 or len(list_of_genes) != Protozoan.NUMBER_OF_GENES:
            self.__genes = 10 * [0]
        else:
            self.__genes = list_of_genes
            
    def get_name(self):
        return self.__name
    
    def get_genes(self):
        return self.__genes
    
    def mutation(self, gene_no, new_gene):
        a = 0
        if 0 <= gene_no <= 9:
            a += 1
        if a > 0:
            if 0 <= new_gene <= 5:
                self.__genes[gene_no] = new_gene
            return True
        else:
            return False
        
    def clone(self, clone_name):
        new_clone = Protozoan(clone_name, self.__genes)
        return new_clone
    
    def mate(self, another_protozoan, descendant_name):
        genes = []
        i = 0
        while i < 10:
            genes.append(self.__genes[i])
            i += 1
            genes.append((another_protozoan.get_genes())[i])
            i += 1
        new_object = Protozoan(descendant_name, genes)
        return new_object
    
    def __str__(self):
        str1 = "Name: {:s}, genes: {:s}".format(self.__name, str(self.__genes))
        return str1