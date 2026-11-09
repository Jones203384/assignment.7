class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency >= self.data[parent_index].urgency:
                break
            self.data[index], self.data[parent_index] = (
                self.data[parent_index],
                self.data[index],
            )
            index = parent_index

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            smallest_index = index

            if (
                left_index < size
                and self.data[left_index].urgency < self.data[smallest_index].urgency
            ):
                smallest_index = left_index
            if (
                right_index < size
                and self.data[right_index].urgency < self.data[smallest_index].urgency
            ):
                smallest_index = right_index

            if smallest_index == index:
                return

            self.data[index], self.data[smallest_index] = (
                self.data[smallest_index],
                self.data[index],
            )
            index = smallest_index

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def remove_min(self):
        if not self.data:
            raise IndexError("remove_min from empty heap")

        minimum = self.data[0]
        last_patient = self.data.pop()
        if self.data:
            self.data[0] = last_patient
            self.heapify_down(0)
        return minimum



# Test your MinHeap class here including edge cases
