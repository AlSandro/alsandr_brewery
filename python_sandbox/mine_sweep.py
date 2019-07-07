
class MineSweeper:

	def mine_sweeper (self, bombs, num_rows, num_cols):
		field = [[ 0 for i in range (num_cols)] for j in range (num_rows)] # add field matrix 
		# print (field)

		for bomb_location in bombs: # add bombs as -1 values
			(bomb_row, bomb_col)  = bomb_location # bomb_row: 0 bomb_col: 0
			field[bomb_row][bomb_col] = -1 # add the -1 to the cell

			row_range = range(bomb_row - 1, bomb_row + 2)  # row_range: range () 
			col_range = range(bomb_col - 1, bomb_col + 2)

			for i in row_range:
				current_i = i
				for j in col_range:
					current_j = j
					if (0 <= i < num_rows) and (0 <= j < num_rows and field[i][j] != -1):
						field[i][j] += 1
		# return '\n'.join(map(str, field))
		return field


mine_sw = MineSweeper()
print (mine_sw.mine_sweeper([[0,1],[0,2],[2, 1]], 4, 4))


