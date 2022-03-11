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
        return this->_list.at(line-1); // we don't start at line 0, we start at line 1
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
        1) Initialize the sets - test cases
        2) Choose the set type for the each test case - execute _SetTypeCreator($type$)
            -> must strictly only use the specified set type for the created set
        3) Fill the two sets with data (based on the $type$ of set you specified.)

*/
private:
    std::string _filename;
    int _test_cases;
    int _type;

public:
    Interface(std::string file){
        this->_filename = file;
        InputFileHandler File(this->_filename);
        File.start_reading();

        this->_test_cases = std::stoi(File._get_line(1));
        if (File._get_line(2).length() == 1)
            this->_type = std::stoi(File._get_line(2));
        else {
            // i lost track to where i am. what am i supposed to do next
        }

    }

    void step_1(){

    }
};

int main(){
    Interface Han("mp1_test.in");

    return 0;
}