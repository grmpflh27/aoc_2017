function knot(cur_pos, skip, list, length)
	list_size = size(list, 1)

   if length == 0 
       cur_pos += skip
       cur_pos %= list_size
       if cur_pos == 0
           cur_pos = 1
       end
       skip += 1
       return cur_pos, skip 
   end
   println("cur_pos: $cur_pos, skip: $skip, length: $length")
   start_idx = cur_pos
   end_idx = cur_pos + length - 1

   # if bigger just split
   if end_idx > list_size
       first_chunk = list[start_idx:end]
       second_chunk = list[1:end_idx%list_size]
       chunk = vcat(first_chunk, second_chunk)
       rev_chunk = reverse(chunk)
       size_first_chunk = size(first_chunk, 1)
       size_second_chunk = size(second_chunk, 1)

       list[start_idx:end] = rev_chunk[1:size_first_chunk]
       list[1:end_idx%list_size] = rev_chunk[end-size_second_chunk+1:end]
   else
		chunk = list[start_idx:end_idx];
		list[start_idx:end_idx] = reverse(chunk)
   end
   
	end_idx = end_idx % list_size;
   
   @show list
   
   #println(list)
   cur_pos += length
   cur_pos += skip
   cur_pos %= list_size
   if cur_pos == 0
           cur_pos = 1
   end	
   skip += 1
   return cur_pos, skip
end


# main function

lengths = [83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100];
list = collect(0:255);

#lengths = [3, 4, 1, 5]
#list = [0, 1, 2, 3, 4]

cur_pos = 1;
skip = 0;

# run knot 2 times
for i in collect(1:size(lengths,1))
    @show i
    cur_pos, skip = knot(cur_pos, skip, list, lengths[i])
end

result = list[1] * list[2];

println("RESULT: $result")
#println(list)