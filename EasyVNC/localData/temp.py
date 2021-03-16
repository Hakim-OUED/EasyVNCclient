# -*- coding: utf-8 -*-
# creation d'une base de doné si elle n'exite pas
import os
import sqlite3, hashlib


class dB:

    def __init__(self):
          self.cheminBd = os.path.dirname(os.path.realpath(__file__)) + '/database.bd'

    # initialisation d'une instance de la BD
    def initDb(self):
        return sqlite3.connect(self.cheminBd)


    # =======================================
    # methode pour creer la table utilisateur
    # =======================================
    def createTableData(self):
        conn = self.initDb()
        try:

            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS data(
                 sessionId = TEXT,
                 userId = TEXT,
                 username TEXT
            )
            """)
            conn.commit()
        # gestion des exeptions
        except sqlite3.OperationalError:
            print('Erreur la table existe deja')
        except sqlite3.DatabaseError:
            print('Erreur de connexion a la BD')
        except Exception as e:
            print("Erreur")
            # self.conn.rollback()
            # annulation de la transaction grace au rollback
        finally:
            conn.close()

        # methode pour inserer un utilisateur
    def insertDonneesUsine(self, name, value):
        conn = self.initDb()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO donneesUsine(name, value) VALUES(?, ?)""", (name, value))
        conn.commit()
        if (cursor.lastrowid):
            print('insertion réussi')
            conn.close()

    def majDonneesUsine(self, name, value):
        conn = self.initDb()
        cursor = conn.cursor()
        retour = cursor.execute("""UPDATE donneesUsine SET value=? where name=?""", (value, name))
        if (retour):
            # print('mise à jour réussi')
            conn.commit()



    # methode pour verifier l'existence d'un mot de passe d un user
    def verificationUser(self, user):
        conn = sqlite3.connect(self.cheminBd)
        cursor = conn.cursor()
        cursor.execute("""SELECT password FROM users WHERE name=?""", (user,))
        password = cursor.fetchone()
        conn.close()
        try:
            for passwd in password:
                hashe = passwd
                return hashe
        except: return None





# =======================================
# test unitaires des CRUD       pour la table user
# =======================================

"""testdb = dB()
testdb.createSuivi()
testdb.createTableUser()
testdb.createDonneesUsine()
# ----test l'insertion d'un user dans la BD
testdb.insertUser("1818","1111")
testdb.insertUser("2019","2019")
testdb.insertUser("1960","1960")

# ---- test insertion es infos de suivis
testdb.insertSuivis("hand", 0)
testdb.insertSuivis("object", 0)
testdb.insertSuivis("volume", 0)

# ----test insertion infos d'usine
testdb.insertDonneesUsine("numserie", "XXXXXX")
testdb.insertDonneesUsine("date", "XXXXXXXX") """

# ----teste le hashage d'un mot de passe

# teste realise avec succes

# ----test creation de la base de données
#testdb.createTableUser()
# teste realise avec succes


# mise a jour du mot de passe admin
# testdb.majMotdepass("12345","12345")

# print(testdb.readUser("admin"))#test de lecture dans la BD

# teste realise avec succes

# ----test si le mot de passe de l'user existe

# if (testdb.verificationUser('john')!=testdb.hashageMotdePasse("bonjour")):
# print('mot de passes existe dans la BD')
# test de la verification de deux hashes realise avec succes

# print(testdb.verificationUser("jeanne"))
# print(testdb.hashageMotdePasse("bonjour"))
# =======================================
# Fin des tests unitaires des CRUD
# =======================================


