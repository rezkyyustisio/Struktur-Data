class StackX:
    max_size = 0
    stack_array = []
    top = 0

    def __init__(self, s):
        self.max_size = s
        self.stack_array = [0] * s
        self.top = -1

    def push(self, j):
        self.top += 1
        self.stack_array[self.top] = j
        return self.stack_array

    def pop(self):
        dummy = self.stack_array[self.top]
        self.top -= 1
        return dummy

    def peek(self):
        return self.stack_array[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size-1

    def delete_element(self, j):
        self.stack_array.remove(j)
        return j

    def search_element(self, j):
        if j in self.stack_array:
            print(str(j)+" Ditemukan")
        else:
            print(str(j)+" tidak ditemukan")

    def edit_element(self, j, k):
        for i in range(len(self.stack_array)):
            if self.stack_array[i] == j:
                self.stack_array[i] = k
                return self.stack_array[i]

    def cari_nilai_total(self):
        return sum(self.stack_array)

    def cari_nilai_rata_rata(self):
        return sum(self.stack_array) / len(self.stack_array)

    def cari_nilai_terbesar(self):
        return max(self.stack_array)

    def cari_nilai_terkecil(self):
        return min(self.stack_array)


class StackApp:

    def __init__(self, jumlah_stack):
        the_stack = StackX(jumlah_stack)
        the_stack.push(20)
        the_stack.push(40)
        the_stack.push(60)
        the_stack.push(80)

        while not the_stack.is_empty():
            value = the_stack.pop()
            print(value, end=" ")
        print("")


my_stack = StackApp(5)
