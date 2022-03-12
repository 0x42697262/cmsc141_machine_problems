// source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1.cpp

/*
    Test Cases: Amount of times creating new two sets.
    Operators: insert, remove, subset, union, intersection, difference, power set

*/

#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <iterator> // i use this for iterating sets ¯\_(ツ)_/¯
#include <bits/stdc++.h> // oh i need this for std::istringstream

class InputFileHandler{
private:
    std::vector<std::string> _list;
    std::string _filename;

public:
    InputFileHandler(std::string filename){
        this->_filename = filename;
    }

    void start_reading(){
        std::ifstream File(this->_filename);
        std::string str;
        
        while(std::getline(File, str)){
            this->_list.push_back(str);
        }
        File.close();
    }
    
    void _print(){
        for(int i=0; i<this->_list.size(); i++) 
            std::cout << this->_list[i] << std::endl;
    }

    std::string _get_line(int line){
        // return this->_list.at(line-1);   // we don't start at line 0, we start at line 1
        return this->_list.at(line);        // due to offset, we don't need to subtract 1 anymore
    }
    
};

template <class SetType>
class Set{
private:
    std::set<SetType> _set_list;

public:
    void _print(){
        for(auto i = this->_set_list.begin(); i != this->_set_list.end(); i++)
            std::cout << *i << std::endl;
    }

    std::set<SetType> _get_type(){
        return this->_set_list;
    }

    void insert(SetType value){
        this->_set_list.insert(value);
    }

    void remove(SetType value){
        this->_set_list.erase(value);
    }

    void subset(){

    }

    void s_union(){


    }

    void intersection(){

    }

    void difference(){


    }

    void power_set(){


    }
};

class Interface{
/*
    This class should be handling how we navigate through the sets. By creating, modifying,
    removing items from a set. An API perhaps?

    Flow:
        0) Initialize the sets like test cases and offset for each test cases
        1) Get the set type
        2) We fill in the two sets with X amount of data
        3) we get the X number of operations and do X operation
        4) Repeat 1
    
    Check the function calculate_offset() for more info

*/
private:
    std::string _filename;
    int _test_cases;
    int _type;
    std::vector<int> _offset;           // we can't tell which line the next case starts so we take its offset for every case
    int _case_id;

public:
    int calculate_offset(){
        // TODO: offset generator for test cases
        return 0;
    }

    Interface(std::string file, int c_id = 0){
        /*
            This is step_0 and step_1, we initiate the test cases and count the offset for each test cases.
        */
        this->_case_id = c_id;
        this->_filename = file;
        InputFileHandler File(this->_filename);
        File.start_reading();


        /*
            This code below stores the set type based on the id number:
            1 : int
            2 : double
            3 : char
            4 : string
            5 : set         ( this a set type ex: [5 1] or [5 3])
            6 : object

            the id number is not used for the sets but rather to keep track of the input
            for type 5, an x amount of recursion might occur if the input is [5 5]
        */

        this->_test_cases = std::stoi(File._get_line( 0 + this->_offset.at(this->_case_id) ));
        if (File._get_line(2).length() == 1)
            this->_type = std::stoi(File._get_line(  1 + this->_offset.at(this->_case_id) ));
        else {
            // i remember now, it's splitting the two numbers
            std::istringstream sub_str(File._get_line(  1 + this->_offset.at(this->_case_id) ));
            std::vector<std::string> v_str;

            std::string temp;
            while (sub_str >> temp)
                v_str.push_back(temp); // this should now have values like [5, 1]

            this->_type = std::stoi(v_str.at(0)); // copy the set type
        }

        // okay we proceed to step 2, fill the set with data...
        this->step_2();
     }

    void step_2(){
        // factory method.... design patterns... meh, let's just use switch case
        switch (this->_type){
        case 1:
            this->step_2_int_type();                
            break;
        
        case 2:
            this->step_2_double_type();                
            break;
        
        case 3:
            this->step_2_char_type();                
            break;
        
        case 4:
            this->step_2_string_type();                
            break;
        
        case 5:
            this->step_2_set_type();                
            break;
        
        case 6:
            this->step_2_objects_type();                
            break;
        
        default:
            break;
        }

    }

    void step_2_int_type(){

    }

    void step_2_double_type(){

    }

    void step_2_char_type(){

    }

    void step_2_string_type(){

    }

    void step_2_set_type(){

    }

    void step_2_objects_type(){
        
    }
};

int main(){
    Interface Han("mp1_test.in");

    return 0;
}