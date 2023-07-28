import pygame
import random
import time

# Dimensões da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

# Cores
DARK_GREEN = (0, 100, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Parâmetros do carro
CAR_WIDTH = 20
CAR_HEIGHT = 10
CAR_SPEED = 3

# Dimensões da rua
ROAD_WIDTH = 800
ROAD_HEIGHT = 13
ROAD_X = (WINDOW_WIDTH - ROAD_WIDTH) // 2
ROAD_Y = WINDOW_HEIGHT // 2

# Espaço entre os carros
SPACE_BETWEEN_CARS = 5

# Quantidade inicial de carros na rua
INITIAL_NUM_CARS = 1

# Faixa de spawn dos novos carros (apenas no lado esquerdo da rua)
SPAWN_LANE_X = ROAD_X + 1

# Classe do carro
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += CAR_SPEED

    def is_out_of_screen(self):
        return self.x > WINDOW_WIDTH

# Função para criar carros aleatoriamente
def create_cars(num_cars, cars):
    while len(cars) < num_cars:
        y = random.randint(ROAD_Y, ROAD_Y + ROAD_HEIGHT - CAR_HEIGHT)

        # Verifica se há espaço no spawn para criar um novo carro
        overlapping = any(abs(car.y - y) < CAR_HEIGHT + SPACE_BETWEEN_CARS and car.x < SPAWN_LANE_X for car in cars)

        if not overlapping:
            car = Car(SPAWN_LANE_X, y)
            cars.append(car)
        else:
            break

    return cars

# Função principal
def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Simulador de Trânsito')
    clock = pygame.time.Clock()

    cars = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        window.fill(DARK_GREEN)

        # Desenha a rua na tela
        pygame.draw.rect(window, WHITE, (ROAD_X, ROAD_Y, ROAD_WIDTH, ROAD_HEIGHT))

        # Movimenta os carros e remove carros fora da tela
        cars = [car for car in cars if not car.is_out_of_screen()]
        for car in cars:
            car.move()

        # Cria novos carros para manter a quantidade inicial
        cars = create_cars(INITIAL_NUM_CARS, cars)

        # Desenha os carros na tela apenas dentro da área da rua
        for car in cars:
            pygame.draw.rect(window, RED, (car.x, car.y, CAR_WIDTH, CAR_HEIGHT))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
