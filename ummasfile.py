{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "### **Composite Data Types**"
      ],
      "metadata": {
        "id": "H_LyNQsTr-1l"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "As a teacher, I have a list of students. Each student has both a favorite color and a lucky number.\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "TGYNYBXyDIoc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# List of students\n",
        "students = [1, \"Amy\", 3]\n",
        "\n",
        "# Dictionary: Storing both the favorite color and favorite lucky for each student.\n",
        "# Here, the value for each student (key) is another dictionary (showcasing the composite nature).\n",
        "student_preferences = {\n",
        "    1: {\"color\": \"Blue\", \"Lucky Number\": 4},\n",
        "    \"Amy\": {\"color\": \"Green\", \"Lucky Number\": 8},\n",
        "    3: {\"color\": \"Red\", \"Lucky Number\": 5}\n",
        "}\n",
        "\n",
        "# Retrieving and printing the favorite color and lucky number for a specific student.\n",
        "student_name = 1\n",
        "print(f\"{student_name}'s favorite color is: {student_preferences[student_name]['color']}\")\n",
        "print(f\"{student_name}'s favorite number is: {student_preferences[student_name]['Lucky Number']}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "56LfYjTEDRJW",
        "outputId": "0832f798-1632-4351-f609-65520327912f"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1's favorite color is: Blue\n",
            "1's favorite number is: 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Functions**"
      ],
      "metadata": {
        "id": "OmuU2t2esaWX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def greet():\n",
        "  print(\"Hello\")\n",
        "greet()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FH2DEpqyDxUd",
        "outputId": "7fc82a94-2fac-47f6-d493-497a80e16d6f"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def greet(name):\n",
        "  print(\"Hi \" + name)\n",
        "greet(\"ame\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OJI9WZDLF4dT",
        "outputId": "b7994e37-a95f-4616-dce8-570f6b177001"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hi ame\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_function(fname, lname): #This is called parameter when you declare the variable in parentheses.\n",
        "  print(fname + \" \" + lname)\n",
        "my_function(\"Emil\", \"Refsnes\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z6SPTEPkGL-t",
        "outputId": "9a07fa49-1119-4096-b9b2-aaf3af326159"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Emil Refsnes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Conditionals**"
      ],
      "metadata": {
        "id": "PeiPh7IIsPsg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a=44\n",
        "b=44\n",
        "if a>b:\n",
        "  print(\"b is big\")\n",
        "elif a==b:\n",
        "  print(\"equal\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3xFShtrFI7dD",
        "outputId": "19abcd87-515d-4488-eb75-d4cf7a586091"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "equal\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Loops**"
      ],
      "metadata": {
        "id": "3Pdz7aX1sVWp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "i=1\n",
        "while i<6:\n",
        "  print(i)\n",
        "  i+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "inPIvc0hKImD",
        "outputId": "ffab1305-af61-478a-f65e-ad4f317b10f4"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Working with Composite Data **"
      ],
      "metadata": {
        "id": "IYcPfdeCZnXs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# These lines import two Python modules:\n",
        "#csv allows you to work with comma-separated values (CSV) files.\n",
        "#copy provides the deepcopy function, which is used to make a deep copy of an object (i.e., a copy that includes all of the object's nested objects).\n",
        "import csv\n",
        "import copy"
      ],
      "metadata": {
        "id": "8PYGP3sCnBue"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "In Python, there are two types of copying: shallow copying and deep copying.\n",
        "\n",
        "Shallow Copy: When you create a shallow copy of an object, you are creating a new object, but the contents (i.e., the references) of the original object are copied to the new object. This means that if the original object contains references to other objects (like lists or dictionaries inside a list), the new object will still point to the same inner objects. So, if you modify these inner objects in the copied object, they will also be modified in the original object.\n",
        "\n",
        "Deep Copy: When you create a deep copy of an object, you are creating a new object along with all the objects that are contained within the original object, recursively. This means that the new object and its contents are entirely independent of the original object. Changes to the inner objects in the copied object will not affect the original object, and vice versa.\n",
        "\n",
        "the shallow copy also modifies the original, but modifying the deep copy does not affect the original."
      ],
      "metadata": {
        "id": "i4Ghe85FpEvv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Example of Shallow/Deep copy\n",
        "import copy\n",
        "\n",
        "# Nested list\n",
        "original_list = [[1, 2, 3], [4, 5, 6]]\n",
        "\n",
        "# Shallow copy\n",
        "shallow_copied_list = copy.copy(original_list)\n",
        "\n",
        "# Deep copy\n",
        "deep_copied_list = copy.deepcopy(original_list)\n",
        "\n",
        "# Modify inner list of shallow copy\n",
        "shallow_copied_list[0][0] = 99\n",
        "\n",
        "# Modify inner list of deep copy\n",
        "deep_copied_list[1][1] = 88\n",
        "\n",
        "print(\"Original:\", original_list)\n",
        "print(\"Shallow Copy:\", shallow_copied_list)\n",
        "print(\"Deep Copy:\", deep_copied_list)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3z7y-FAWpXCP",
        "outputId": "ab2878fc-c5f8-4e74-e829-b2947110ae6f"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original: [[99, 2, 3], [4, 5, 6]]\n",
            "Shallow Copy: [[99, 2, 3], [4, 5, 6]]\n",
            "Deep Copy: [[1, 2, 3], [4, 88, 6]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# This sets up a dictionary named myVehicle that represents a vehicle's attributes. Each attribute has a default value.\n",
        "myVehicle = {\n",
        "    \"vin\" : \"<empty>\",\n",
        "    \"make\" : \"<empty>\" ,\n",
        "    \"model\" : \"<empty>\" ,\n",
        "    \"year\" : 0,\n",
        "    \"range\" : 0,\n",
        "    \"topSpeed\" : 0,\n",
        "    \"zeroSixty\" : 0.0,\n",
        "    \"mileage\" : 0\n",
        "}"
      ],
      "metadata": {
        "id": "pJZm9QpenNPl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# This loop goes through each key-value pair in the myVehicle dictionary and prints them out.\n",
        "for key, value in myVehicle.items():\n",
        "    print(\"{} : {}\".format(key,value))"
      ],
      "metadata": {
        "id": "hxrJxt8xqw_B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# This initializes an empty list named myInventoryList. This list will be used to store the vehicles from the CSV file.\n",
        "myInventoryList = []"
      ],
      "metadata": {
        "id": "55mQeYvwnZQi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# This opens a CSV file named 'car_fleet.csv' and assigns its contents to the variable csvFile.\n",
        "#This creates a csv.reader object named csvReader that will allow you to read the contents of the CSV file. The delimiter is specified as a comma.\n",
        "with open('car_fleet.csv') as csvFile:\n",
        "      csvReader = csv.reader(csvFile, delimiter=',')\n",
        "      # This initializes a variable named lineCount to zero. It's used to count the number of rows processed in the CSV file.\n",
        "      lineCount = 0\n",
        "      # This loop iterates over each row in the csvReader object (i.e., each line in the CSV file).\n",
        "      for row in csvReader:\n",
        "        if lineCount == 0:\n",
        "            print(f'Column names are: {\", \".join(row)}')\n",
        "            # This checks if the current row is the first row of the CSV file (the header). If it is, the program prints the column names. Then, it increments the lineCount variable.\n",
        "            lineCount += 1\n",
        "# For all other rows (not the header), this prints the contents of each column.\n",
        "        else:\n",
        "            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')\n",
        "            # This makes a deep copy of the myVehicle dictionary and assigns it to the variable currentVehicle.\n",
        "            currentVehicle = copy.deepcopy(myVehicle)\n",
        "# assign the values from the current row of the CSV file to the corresponding keys in the currentVehicle dictionary.\n",
        "            currentVehicle[\"vin\"] = row[0]\n",
        "            currentVehicle[\"make\"] = row[1]\n",
        "            ...\n",
        "            currentVehicle[\"mileage\"] = row[7]\n",
        "# This appends the currentVehicle dictionary to the myInventoryList.\n",
        "            myInventoryList.append(currentVehicle)\n",
        "            # This increments the lineCount variable to keep track of the number of rows processed.\n",
        "            lineCount += 1\n",
        "            # After processing all rows in the CSV file, this line prints the total number of rows processed.\n",
        "            print(f'Processed {lineCount} lines.')\n",
        "# This line makes another deep copy of the myVehicle dictionary, but it seems unnecessary since currentVehicle is already updated within the loop and is not used after this point.\n",
        "currentVehicle = copy.deepcopy(myVehicle)\n",
        "# This nested loop goes through each vehicle in the myInventoryList and prints out its attributes (key-value pairs). Each attribute is separated by a line of dashes.\n",
        "for myCarProperties in myInventoryList:\n",
        "    for key, value in myCarProperties.items():\n",
        "        print(\"{} : {}\".format(key,value))\n",
        "        print(\"-----\")\n",
        "# In summary, this code reads vehicle data from a CSV file, processes it, stores it in a list of dictionaries, and then prints out each vehicle's attributes."
      ],
      "metadata": {
        "id": "2DuGph1HneRh"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}