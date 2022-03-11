// source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1.cpp

#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

template <class SetType>
class Set{
private:
    std::vector<std::string> _list;
    std::string _filename;

public:
    Set(std::string filename){
        this->_filename = filename;
        std::cout << this->_filename;
    }

    void start_reading(){
        std::ifstream File(this->_filename);
        std::string str;
        while(std::getline(File, str)){
            this->_list.push_back(str);
        }
    }
    
    void something(){
        for(int i=0; i<this->_list; i++) std::cout << this->_list[i];
    
    }
    
};

int main(){
    Set<int> fuck("shit");

    return 0;
}