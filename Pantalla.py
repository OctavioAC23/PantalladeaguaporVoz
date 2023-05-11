import pygame
import sys

# Función que muestra la forma de deletreo correspondiente a una letra
def mostrar_forma_deletreo(letra):
        if letra == 'a' or letra == 'á' or letra == 'A':
            Mostrar(a_shape)
        elif letra == 'b'or letra == 'B':
            Mostrar(b_shape)
        elif letra == 'c'or letra == 'C':
            Mostrar(c_shape)
        elif letra == 'd'or letra == 'D':
            Mostrar(d_shape)
        elif letra == 'e'or letra == 'é'or letra == 'E':
            Mostrar(e_shape)
        elif letra == 'f'or letra == 'F':
            Mostrar(f_shape)
        elif letra == 'g'or letra == 'G':
            Mostrar(g_shape)
        elif letra == 'h'or letra == 'H':
            Mostrar(h_shape)
        elif letra == 'i'or letra == 'í'or letra == 'I':
            Mostrar(i_shape)
        elif letra == 'j'or letra == 'J':
            Mostrar(j_shape)
        elif letra == 'k'or letra == 'K':
            Mostrar(k_shape)
        elif letra == 'l'or letra == 'L':
            Mostrar(l_shape)
        elif letra == 'm'or letra == 'M':
            Mostrar(m_shape)
        elif letra == 'n'or letra == 'N':
            Mostrar(n_shape)
        elif letra == 'o'or letra == 'ó'or letra == 'O':
            Mostrar(o_shape)
        elif letra == 'p'or letra == 'P':
            Mostrar(p_shape)
        elif letra == 'q'or letra == 'Q':
            Mostrar(q_shape)
        elif letra == 'r'or letra == 'R':
            Mostrar(r_shape)
        elif letra == 's'or letra == 'S':
            Mostrar(s_shape)
        elif letra == 't'or letra == 'T':
            Mostrar(t_shape)
        elif letra == 'u'or letra == 'ú'or letra == 'U':
            Mostrar(u_shape)
        elif letra == 'v'or letra == 'V':
            Mostrar(v_shape)
        elif letra == 'w'or letra == 'W':
            Mostrar(w_shape)
        elif letra == 'x'or letra == 'X':
            Mostrar(x_shape)
        elif letra == 'y'or letra == 'Y':
            Mostrar(y_shape)
        elif letra == 'z'or letra == 'Z':
            Mostrar(z_shape)

        Borrar()

        

def Borrar():
    # Borra toda la pantalla
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen_width, screen_height))
    pygame.display.update()

def Mostrar(shape):
    # Borra la pantalla antes de mostrar la forma
    Borrar()

    # Mostrar la forma desde abajo hacia arriba
    for i in range(len(shape)-1, -1, -1):
        for k in range(i+1):
            for j in range(len(shape[0])):
                if shape[i-k][j]:
                    grid[i-k][j] = 1
                    pygame.draw.rect(screen, (0, 0, 0), (j*cell_size, (i-k)*cell_size, cell_size, cell_size))
            pygame.display.update()
            pygame.time.wait(50)  # Ajustar tiempo de espera para controlar la velocidad de animación
        
        # Esperar un momento antes de borrar la fila
        pygame.time.wait(75)
    
    # Borra toda la forma gradualmente
    for i in range(len(shape)):
        for k in range(len(shape)-i):
            for j in range(len(shape[0])):
                if shape[len(shape)-1-k-i][j]:
                    grid[len(shape)-1-k-i][j] = 0
                    pygame.draw.rect(screen, (255, 255, 255), (j*cell_size, (len(shape)-1-k-i)*cell_size, cell_size, cell_size))
            pygame.display.update()
            pygame.time.wait(50)  # Ajustar tiempo de espera para controlar la velocidad de animación

# Configuración de la pantalla
cell_size = 40
grid_size = 8
screen_width = cell_size * grid_size
screen_height = cell_size * grid_size
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dibujando")

# Configuración de la cuadrícula
grid_color = (255, 255, 255)
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
a_shape = [
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
b_shape = [
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
c_shape = [
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
d_shape = [
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
e_shape = [
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
f_shape = [
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
g_shape = [
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
h_shape = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
i_shape = [
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
]
j_shape = [
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
k_shape = [
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
l_shape = [
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
m_shape = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
n_shape = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
o_shape = [
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
p_shape = [
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
q_shape = [
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
r_shape = [
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
s_shape = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
t_shape = [
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
u_shape = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
v_shape = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
w_shape = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
x_shape = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
y_shape = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
z_shape = [
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
# Dibujado de la cuadrícula y de la letra A
def draw_grid():
    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen, grid_color, (0, y), (screen_width, y))

def draw_letter():
    for i in range(len(a_shape)):
        for j in range(len(a_shape[0])):
            if a_shape[i][j]:
                grid[grid_size-len(a_shape)+i][int(grid_size/2)-int(len(a_shape[0])/2)+j] = 1

# Obtener los argumentos
args = sys.argv[1:]  # Ignoramos el primer argumento, que es el nombre del archivo

# Asignar los argumentos a las variables correspondientes
Peticion = args[0]
imp = args[1]

# Bucle principal
draw_grid()
showing_a = True
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Actualización de la pantalla
    for i in range(grid_size):
        for j in range(grid_size):
            color = (255, 255, 255) if grid[i][j] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j*cell_size, i*cell_size, cell_size, cell_size))
    
    pygame.display.update()
    if Peticion == 'vocales':
        letras = [a_shape,e_shape,i_shape,o_shape,u_shape]
        for letra in letras:
            Mostrar(letra)
            Borrar()
    elif Peticion == 'alfabeto':
        letras = [a_shape, b_shape, c_shape, d_shape, e_shape, f_shape, g_shape, h_shape, i_shape, j_shape, k_shape, l_shape, m_shape, n_shape, o_shape, p_shape, q_shape, r_shape, s_shape, t_shape, u_shape, v_shape, w_shape, x_shape, y_shape, z_shape]
        for letra in letras:
            Mostrar(letra)
            Borrar()
    elif Peticion == 'deletrea':
            for letra in imp:
                mostrar_forma_deletreo(letra)
    pygame.quit()
    quit()
