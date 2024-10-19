import heapq

def min_cost_to_connect_cables_with_order(cables):
    # Перетворюємо список довжин кабелів на мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    order = []
    
    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменші елементи з купи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислюємо витрати на їх з'єднання
        cost = first + second
        
        # Додаємо ці витрати до загальних витрат
        total_cost += cost
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(cables, cost)
        
        # Додаємо пару кабелів до списку порядку об'єднання
        order.append((first, second))
    
    return total_cost, order

# Приклад використання
cables = [4, 3, 2, 6]
total_cost, order = min_cost_to_connect_cables_with_order(cables)
print(f"Загальні витрати: {total_cost}")
print("Порядок об'єднання:", order)