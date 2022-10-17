from cmath import sqrt
class Punto:
    def __init__ (self, ejex=0, ejey=0):
        self.ejex = ejex
        self.ejey = ejey

    def __str__(self):
        return f"({self.ejex},{self.ejey}"

    def cuadrante(self):
        if self.ejex==0 and self.ejey==0:
            print(f"El punto {self} se encuentra en el eje de abscisas")
        elif self.ejex>0 and self.ejey>0:
            print (f"El punto {self} se encuentra en el primer cuadrante")
        elif self.ejex<0 and self.ejey>0:
            print(f"El punto {self} se encuentra en el segundo cuadrante")
        elif self.ejex<0 and self.ejey<0:
            print(f"El punto {self} se encuentra en el tercer cuadrante")
        elif self.ejex>0 and self.ejey<0:
            print(f"El punto {self} se encuentra en el cuarto cuadrante")
        elif self.ejex==0 and self.ejey!=0:
            print(f"El punto {self} se encuentra en el eje Y")
        else:
            print(f"El punto {self} se encuentra en el eje X")
    def vector(self,punto2):
        return(f"El vector de los puntos {self} y {punto2} es ({punto2.ejex - self.ejex},{punto2.ejex - self.ejex})")
    def distancia(self,punto3):
        dist= sqrt((punto3.ejex - self.ejex)**2 + (punto3.ejex - self.ejex)**2)
        return(f"La distancia entre {self} y {punto3} es {dist} ")
class Rectangulo:
    def __init__(self,inicial=Punto(),final=Punto()):
        self.inicial=inicial
        self.final=final
    def base(self,inicial=Punto(),final=Punto()):
        self.Base=abs(self.final.ejex-self.inicial.ejex)
        return(f"La base del rectangulo es {self.Base}")
    def altura(self,inicial=Punto(),final=Punto()):
        self.Altura=abs(self.final.ejey-self.inicial.ejey)
        return(f"La altura del rectangulo es {self.Altura}")
    def area(self,inicial=Punto(),final=Punto()):
        self.Area=abs(self.Base * self.Altura)
        return(f"El area del rectangulo es {self.Area}")
A=Punto(2,3)
B=Punto(5,5)
C=Punto(-3,-1)
D=Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

rectangulo=Rectangulo(A,B)
rectangulo.base()
rectangulo.altura()
rectangulo.area()



