class pcy_algo:
    def __init__(self, transaction_data, unique_item_sets,hash_func_size,support,confidence):
        self.num_transactions = transaction_data
        self.unique_item_sets = unique_item_sets
        self.size = hash_func_size
        self.support = support
        self.confidence = confidence
        
    def pass_one(self):
        items_count = {}
        for row in self.num_transactions:
           for item in row:
               if item in items_count:
                  items_count[item] = items_count[item] + 1
               else:
                  items_count[item] = 1
        return items_count
    
    def pass_one_filter(self,items_count):
        for i in range(0,len(items_count)):
           key = i + 1
           count = items_count[key]
           if count < self.support:
             del items_count[key]
           else:
             continue
        return items_count

    
    def pass_two(self,items_count):  
        candidate_sets = {}
        hash_func = [0]*self.size
        bit_vector = [0]*self.size
        final_sets = []
        for row in self.num_transactions:
            basket = row
            for i in range(0,len(basket)-1,1):
              for j in range(i+1,len(basket),1):
                 item_pair = [basket[i],basket[j]]
                 if basket[i] in items_count and basket[j] in items_count:
                    hash_index = (basket[i]*basket[j])%self.size
                    if hash_index in candidate_sets:
                       temp = candidate_sets[hash_index]
                       if item_pair not in temp:
                         candidate_sets[hash_index].append(item_pair)
                    else:
                        candidate_sets[hash_index] = [item_pair]
                    hash_func[hash_index] = hash_func[hash_index] + 1
                 else:
                   continue
        for i in range(len(hash_func)):
            if hash_func[i] >= self.support:
               bit_vector[i] = 1

        for i in range(len(bit_vector)):
            if bit_vector[i] == 1:
               for item_set in candidate_sets[i]:
                   final_sets.append(item_set)
        return final_sets 
    
    def support1(self,item_pair):
      no_of_transac_x_and_y = 0
      for row in self.num_transactions:
         hash = {
         item_pair[0]:0,
         item_pair[1]:0
         }
         for item in row:
           if item in hash:
              hash[item] = hash[item]+1
         if hash[item_pair[0]] >= 1 and hash[item_pair[1]] >= 1:
            no_of_transac_x_and_y = no_of_transac_x_and_y + 1
      return no_of_transac_x_and_y/len(self.num_transactions)

    def support2(self,input_item):
       no_of_transac = 0
       for row in self.num_transactions:
         is_present = False
         for item in row:
            if item == input_item:
               is_present = True
         if is_present:
            no_of_transac = no_of_transac + 1
       return no_of_transac/len(self.num_transactions)
    
    def filter_by_confidence(self,final_sets):
        final_item_pair = []
        for item_set in final_sets:
           conf1 = (self.support1(item_set)/self.support2(item_set[0]))*100
           conf2 = (self.support1(item_set)/self.support2(item_set[1]))*100
           if conf1 > self.confidence:
              final_item_pair.append([item_set[0],item_set[1],conf1])
           if conf2 > self.confidence:
              final_item_pair.append([item_set[1],item_set[0],conf2])
        return final_item_pair
    
    def mine_data(self):
       items_count = self.pass_one()
       items_count = self.pass_one_filter(items_count)
       final_sets  = self.pass_two(items_count)
       final_pairs = self.filter_by_confidence(final_sets)
       return final_pairs


        
