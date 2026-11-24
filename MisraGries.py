from pyspark.sql import SparkSession
import ConvertToCompatible

def set_up():

    spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Test") \
    .getOrCreate()

    df = spark.read.parquet(str(ConvertToCompatible.converter()))

    return df

def misra_gries(df,k):

    counter_dict = {}
    
    column = "Opening"
    for row in df.select(column).toLocalIterator():
            item = row[column]
            increment(item,counter_dict,k)
            print(row)

    return counter_dict

def increment(item, counter_dict, k):

    if item in counter_dict:
         counter_dict[item] += 1

    elif len(counter_dict) < k -1:
        counter_dict[item] = 1

    else:
        decrement(counter_dict)


def decrement(counter_dict):
    for item in list(counter_dict):
        counter_dict[item] -= 1

        if counter_dict[item] == 0:
            counter_dict.pop(item)

             
         
     
def main():

    counter_dict = misra_gries(set_up(),100)

    frequent_candidate = max(counter_dict, key=counter_dict.get)

    print(f"The most Frequent Item Candidate is: {frequent_candidate}")
    print("-------------------")
    print("---------+---------")
    print(counter_dict)

main()

