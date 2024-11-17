import csv


def total_sum(directory,namefile):

    with open(directory, 'r') as file_prodyct:
        data = csv.DictReader(file_prodyct)

        save_data = {}

        for line in data:
            prodyct = line['product']
            total_price = int(line['quantity']) * float(line['price'])

            if prodyct in save_data:
                save_data[prodyct] += total_price

            else: 
                save_data[prodyct] = total_price





    with open (namefile, "w", newline="") as file_total_sum:

        writecvs = csv.DictWriter(file_total_sum, fieldnames=['product','sum_price'])
        
        writecvs.writeheader()

        for product, total_sales in save_data.items():
            writecvs.writerow({'product' : product , 'sum_price': total_sales})
       




if __name__ == "__main__":

    total_sum('files/zad_4/sales.csv','total_sum.csv')