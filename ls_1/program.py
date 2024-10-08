def craate_img(list):
    img = ''
    for col in range(list[0]+1):
        for row in range(list[1]+1):
            if row == 0 or row == list[1]:
                img += '|'
            elif col == 0 or col == list[0]:
                img += '-'
            else:
                img += ' '
        img +='\n'
    return img
def take_w_h():
    wihgh = int(input('wihgh:'))
    height = int(input('height:'))
    return height, wihgh


print(craate_img(take_w_h()))