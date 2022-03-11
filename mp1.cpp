// source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1.cpp

#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

template <class SetType>
class InputFileHandler{
private:
    std::vector<std::string> _list;
    std::string _filename;

public:
    Set(std::string filename){
        this->_filename = filename;
    }

    void start_reading(){
        std::ifstream File(this->_filename);
        std::string str;
        
        while(std::getline(File, str)){
            this->_list.push_back(str);
        }
    }
    
    void _print(){
        for(int i=0; i<this->_list.size(); i++) 
            std::cout << this->_list[i] << std::endl;
    }

    std::string _get_line(int line){
        return this->_list.at(line);
    }
    
};

int main(){
    

    return 0;
}