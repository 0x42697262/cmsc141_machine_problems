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
    InputFileHandler(std::string filename = ""){
        if ( !filename.empty() )
            this->_filename = filename;
    }

    void set_filename(std::string filename){
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

    std::vector<std::string> get_list(){
        return this->_list;
    }
    
    void _print(){
        for(int i=0; i<this->_list.size(); i++) 
            std::cout << this->_list[i] << std::endl;
    }

    std::string _get_line(int line){
        return this->_list.at(line-1);   // we don't start at line 0, we start at line 1
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

    std::set<SetType> _get_list(){
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
        0) Initialize the sets like test cases
        1) Get the set type
        2) We fill in the two sets with X amount of data
        3) we get the X number of operations and do X operation
        4) Repeat 1
    
*/
private:
    std::string _filename;
    InputFileHandler File;

    int _test_cases;
    int _type;
    int _case_id;

public:
    Interface(std::string file){
        /*
            We set the filename and read its contents then get its test cases.
        */
        this->_filename = file;
        this->File.set_filename(file);
        this->File.start_reading();
        this->_test_cases = std::stoi(File._get_line(1));
        this->_case_id = 0;

        this->step_0(this->_case_id);
    }

    void step_0(int case_id){
        /*



        */


        if (File._get_line(2).length() == 1)
            this->_type = std::stoi(File._get_line(2));
        else {
            std::istringstream sub_str(File._get_line(2));
            std::vector<std::string> v_str;

            std::string temp;
            while (sub_str >> temp)
                v_str.push_back(temp); // this should now have values like [5, 1]

            this->_type = std::stoi(v_str.at(0)); // copy the set type
        }
    }
    
};

int main(){
    Interface Han("mp1_test.in");

    return 0;
}