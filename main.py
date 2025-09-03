import os
import heapq

class AlgoritmoHuffman:
    def __init__(self, path):
        self.path = path
        self.heap = [] #Fila de Prioridade
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        # defining comparators less_than and equals
        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if(other == None):
                return False
            if(not isinstance(other, self.HeapNode)):
                return False
            return self.freq == other.freq
    
    def make_frequency_dict(self, text):
                frequency = {}     
                for char in text:
                        if char not in frequency:
                            frequency[char] = 0
                        frequency[char] += 1
                return frequency

    def make_heap(self, frequency):
                for caracter in frequency:
                        node = self.HeapNode(caracter, frequency[caracter])
                        heapq.heappush(self.heap, node)
                # for i in self.heap:
                #         print(i.freq)

    def merge_nodes(self):
                while(len(self.heap) > 1):
                        node1 = heapq.heappop(self.heap)
                        node2 = heapq.heappop(self.heap)

                        new_node = self.HeapNode(None, node1.freq + node2.freq)

                        new_node.left = node1
                        new_node.right = node2
                        
                        heapq.heappush(self.heap, new_node)
                
    # def make_codes_helper(self, tree, current_code):
    #             if(tree == None):
    #                    return
                
    #             if(tree.char != None):
    #                    self.codes
    
    # def make_codes(self):
    #             tree = heapq.heappop(self.heap)
    #             self.make_codes_helper(tree, "")
                







    def compress(self):
                filename, file_extension = os.path.splitext(self.path)
                output_path = filename + ".bin"

                with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
                        text = file.read()
                        text = text.rstrip()

                        frequency = self.make_frequency_dict(text)
                        print(frequency)
                        self.make_heap(frequency)
                        self.merge_nodes()
                        print(self.heap[0].char)

                        print(self.heap[0].right.char)
                        print(self.heap[0].right.left.char)
                        print(self.heap[0].right.right.left.char)

                        print(self.heap[0].right.right.right.char)

                #         self.make_codes()

                #         encoded_text = self.get_encoded_text(text)
                #         print(encoded_text)
                #         padded_encoded_text = self.pad_encoded_text(encoded_text)
                #         print(padded_encoded_text)


                #         b = self.get_byte_array(padded_encoded_text)
                #         print(b)

                #         output.write(bytes(b))

                # print("Compressed")
                # return output_path
h = AlgoritmoHuffman('texto_exemplo.txt')
h.compress()
