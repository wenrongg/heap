# helper functions

def left(index):
    '''Return index's left child index.
    '''
    return index * 2 + 1


def right(index):
    '''Return index's left child index.
    '''
    return index * 2 + 2
    
    
def parent(index):
    '''Return index's parent index.'''
    
    return (index - 1) // 2


class MinHeap:
    def __init__(self, L: list):
        '''Create a new MinHeap'''
        self._tree = []
        
    def __len__(self):
        return len(self._tree)
    
    
    def insert(self, v):
        '''Insert v in self. Maintain heap property.'''
        
        # insert at the end to maintain completeness property
        # restore heap property
        pass
    
    
    def extract_min(self):
        '''Remove minimal value in self. Restore heap property.'''
        
        # swap first and last element
        # remove last element to maintain completeness property
        # restore heap property
        # return min value
        pass
    
    
    def _percolate_up(self, i):
        '''Restore heap property of self after 
        adding new item at index i'''
        
        # while larger than parent
        # swap with parent
        pass
    
    
    def _percolate_down(self, i):
        ''' Restore heap property of subtree 
        rooted at index i.
        '''
        
        # while larger than at least one child
        # swap with smaller child and repeat
        
        pass
    
    def _min_heapify(self):
        '''Turn unordered list into min-heap.'''
        
        # for each node in the first half of the list
        # percolate down to
        pass
    