def main():

    class Robot():

     articulaciones = ["base","hombro","brazo","antebrazo","mano"]
     nombre_robot = str('Brazo Robotico')

     def set_name (self):
      Nombre = input("Cambie el nombre del manipulador ")

     def getname(Nombre):
        print(Nombre)

    pose = Robot()
    print(pose.nombre_robot)
    pose.set_name()
    print(pose.articulaciones)

if __name__ == "__main__":
    main()