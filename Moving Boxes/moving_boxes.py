"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 50358236
Name:       Ngoc Mai Nguyen
Email:      mai.n.nguyen@tuni.fi
The programm consists different operations on the Moving box. 
Methods from this programm can be used to moving items, adding items, listing items, 
removing items, etc. from the Moving box.
"""


class MovingBox:
    """
    A class for keeping track of the contents of
    a moving box. Items can be added to, removed from,
    itemized (i.e. listed), and searched from a moving box.
    The number of items in a box can also be queried
    and items can be transferred between two boxes.
    """

    def __init__(self, name):
        """
        construct a object with the properties:

          __name = name (first argument of the constructor function): the name of
                                          the box object

          __list_of_items: a dictionary of list of items and their quantities to
                           keep track of the state of the box

          __number_of_items: a int to keep track of the total number of items currently
                             in the box named
        """
        self.__name = name
        self.__list_of_items = {}
        self.__number_of_items = 0
        pass

    def add_item(self, name, number):
        """
        This function is used to add items in to the box
        :param name: the name of the items to be added to the box
        :param number: number of the quantity of the items to be added to the box
        :return: None
        """

        self.__number_of_items += number

        if name not in self.__list_of_items:
            self.__list_of_items[name] = number
        else:
            self.__list_of_items[name] += number
        return

    def remove_item(self, name, number):
        """
        The function is used to remove the items from the box
        :param name: the name of the items to be removed from the box
        :param number: numer of the quantity of the items to be removed from the box
        return: boolean
                True if the removation happens smoothly
                False if the removation can't happen
        """
        if name not in self.__list_of_items:
            return False
        if self.__list_of_items[name] < number:
            return False

        self.__number_of_items -= number
        self.__list_of_items[name] -= number

        if self.__list_of_items[name] == 0:
            self.__list_of_items.pop(name)

        return True

    def transfer_item(self, other, name, count):
        """
        The function is used to transferred a certain amount of items from 1 box to another box
        :param other: targeted box
        :param name: the name of the items to be transferred from the box
        :param count: number of the items to be transferred
        :return: boolean
                True if the transfer process happens smoothly
                False if the transfer process can't happen
        """
        if name not in self.__list_of_items:
            return False
        if self.__list_of_items[name] < count:
            return False

        other.add_item(name, count)

        self.remove_item(name, count)

        return True

    def list_content(self):
        """
        The function prints a list of content of the box
        :param: None
        :return: None
        """
        print(f"Box \"{self.__name}\" contains {self.__number_of_items} items.")

        for key in sorted(self.__list_of_items.keys()):
            to_print = str(self.__list_of_items[key]).rjust(3, " ")
            print(f"{to_print} {key}")

        return

    def search_item(self, name):
        """
        This function is used to search for the amount of the item asked
        :param name: the name of the item to be searched in the box
        :return: integer
                The amount of amount of the item can be found
        """
        return 0 if name not in self.__list_of_items else self.__list_of_items[name]


def convert_str_to_int(word):
    """
    Converts the parameter string *word* in to an integer value.
    If conversion is successful returns the resulting integer.
    In the case of an error, returns None.

    :param (str) word: a word supposedly representing an integer value.
    :return: int | NoneType
    """
    try:
        result = int(word)
    except ValueError:
        return None

    return result


def newbox(all_boxes, list_of_additional_info):
    """
    Creates a new moving box named after the first element in
    the parameter *list_of_additional_info*. The new box is stored
    in the dictionary *all_boxes* using the box's name as the key.
    If *all_boxes* already contains a box with the same name,
    it will be removed and replaced with the new box.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing a single element:
           the name of the moving box (str) to be created.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of initial data: can't create a new box.")
        return

    box_name = list_of_additional_info[0]
    all_boxes[box_name] = MovingBox(box_name)


def add_to_box(all_boxes, list_of_additional_info):
    """
    Adds a new item into a box stored in the dictionary *all_boxes*.
    If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is shown.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 3 elements:
           the name of the box (str),
           the name of the item (str), and
           the number of items to be added (str).
    :return: None
    """

    if len(list_of_additional_info) != 3:
        print("Error: wrong number of elements: can't add into a box.")
        return

    box_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't add to a box.")
        return

    if box_name not in all_boxes:
        print("Error: box does not exist: can't add to a box.")
        return

    all_boxes[box_name].add_item(item_name, item_count)


def remove_from_box(all_boxes, list_of_additional_info):
    """
    Removes a given amount of named items from a box stored
    in the dictionary *all_boxes*.
    If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is displayed.
    If the box exits but doesn't contain the named item,
    then an error message is also displayed.
    If the parameter giving the number of items to be removed
    is larger than what's available in the box, then again
    an error message is displayed.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 3 elements:
           the name of the box (str),
           the name of the item (str), and
           the number of items to be removed (str).
    :return: None
    """

    if len(list_of_additional_info) != 3:
        print("Error: wrong number of elements: can't remove from a box.")
        return

    box_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't remove from a box.")
        return

    if box_name not in all_boxes:
        print("Error: box does not exist: can't remove from a box.")
        return

    if not all_boxes[box_name].remove_item(item_name, item_count):
        print("Error: removing an item from a box failed.")


def transfer_from_box_to_another_box(all_boxes, list_of_additional_info):
    """
    Transfers some amount of named items from one moving box to into another.

    :param all_boxes: all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 4 elements:
           the name of the source box (str),
           the name of the target box (str),
           the name of the item to move (str), and
           the number of items to move (str)
    :return: None
    """

    if len(list_of_additional_info) != 4:
        print("Error: wrong number of elements: can't transfer items.")
        return

    source_name, target_name, item_name, item_count = list_of_additional_info
    item_count = convert_str_to_int(item_count)

    if item_count is None:
        print("Error: not a number: can't transfer items.")
        return

    if source_name not in all_boxes or target_name not in all_boxes:
        print("Error: unknown box name: can't transfer items.")

    if not all_boxes[source_name].transfer_item(all_boxes[target_name], item_name, item_count):
        print("Error: item transfer failed for some reason.")


def list_box_content(all_boxes, list_of_additional_info):
    """
    Displays the contents of a single box in *all_boxes*
    dictionary. If there is no box named by the first element of the list
    *list_of_additional_info*, then an error message is displayed.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing 1 element:
           the name of the box (str)
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't list contents.")
        return

    box_name = list_of_additional_info[0]

    if box_name not in all_boxes:
        print("Error: box does not exist: can't list content.")
        return

    all_boxes[box_name].list_content()


def list_all_boxes(all_boxes, list_of_additional_info):
    """
    Prints the contents of all boxes on the screen.
    The boxes are printed in an alphabetical order.
    The content of each individual box is printed
    in the same format as it is done in the function
    *list_box_content* above.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: An empty list since this function
           does not require any other data than *all_boxes*.
    :return: None
    """

    if len(list_of_additional_info) != 0:
        print("Error: wrong number of elements: boxes not listed.")
        return

    for box_name in sorted(all_boxes):
        list_box_content(all_boxes, [box_name])


def search_all_boxes(all_boxes, list_of_additional_info):
    """
    Searches a particular item in all of the boxes and
    and prints which boxes contained the item and how
    many of it there was. The boxes in *all_boxes* are
    checked in an alphabetical order. If no items are found,
    the function prints nothing.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing one element (str)
           which is the name of the item the function should search for.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't search boxes.")
        return

    item_name = list_of_additional_info[0]

    for box_name in sorted(all_boxes):
        item_count = all_boxes[box_name].search_item(item_name)

        if item_count > 0:
            print(f"Box {box_name}: {item_count}")


def count_specific_items(all_boxes, list_of_additional_info):
    """
    Counts and prints the number of a particular items
    inside all of the boxes contained in *all_boxes*.
    Zero is printed if there are none.

    :param all_boxes: A dictionary containing moving box objects.
           The name of the box is used as the key.
    :param list_of_additional_info: A list containing one element (str)
           which is the name of the item the function should count.
    :return: None
    """

    if len(list_of_additional_info) != 1:
        print("Error: wrong number of elements: can't count items.")
        return

    item_name = list_of_additional_info[0]

    item_count = 0
    for box in all_boxes.values():
        item_count += box.search_item(item_name)

    print(f"There are total {item_count} {item_name}(s) in the boxes.")


def main():
    """
    In this project *main* function contains the top level
    part of the program's user interface.
    """
    boxes = {}

    while True:
        command_line = input("next command> ").strip()
        if command_line == "":
            break

        command_words = command_line.split()
        first_word = command_words[0]
        list_of_other_words = command_words[1:]

        if first_word == "quit":
            break

        elif first_word == "newbox":
            newbox(boxes, list_of_other_words)

        elif first_word == "add":
            add_to_box(boxes, list_of_other_words)

        elif first_word == "remove":
            remove_from_box(boxes, list_of_other_words)

        elif first_word == "transfer":
            transfer_from_box_to_another_box(boxes, list_of_other_words)

        elif first_word == "list":
            list_box_content(boxes, list_of_other_words)

        elif first_word == "list_all":
            list_all_boxes(boxes, list_of_other_words)

        elif first_word == "search":
            search_all_boxes(boxes, list_of_other_words)

        elif first_word == "count":
            count_specific_items(boxes, list_of_other_words)

        else:
            print(f"Error: \"{first_word}\" is not a recognized command!")


if __name__ == "__main__":
    main()
