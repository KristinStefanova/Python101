#include <iostream>
#include <cstring>
#include <string>
#include <fstream>

using namespace std;

class Jedi {

    char* name;
    char* rank;
    char* spicies;
    char* militaryRank;
    double midiChlorian;


public:

    Jedi()
    {

        this->name = nullptr;
        this->rank = nullptr;
        this->spicies = nullptr;
        this->militaryRank = nullptr;
        this->midiChlorian = 0;

    }

    Jedi(const char* name, const char* rank, const char* spicies, const char* militaryRank, double midiChlorian) {

        this->name = new char[strlen(name) + 1];
        strcpy(this->name, name);

        this->rank = new char[strlen(rank) + 1];
        strcpy(this->rank, rank);

        this->spicies = new char[strlen(spicies) + 1];
        strcpy(this->spicies, spicies);

        this->militaryRank = new char[strlen(militaryRank) + 1];
        strcpy(this->militaryRank, militaryRank);

        this->midiChlorian = midiChlorian;


    }
    Jedi(const Jedi &other)
    {
        this->name = new char[strlen(other.name) + 1];
        strcpy(this->name, other.name);

        this->rank = new char[strlen(other.rank) + 1];
        strcpy(this->rank, other.rank);

        this->spicies = new char[strlen(other.spicies) + 1];
        strcpy(this->spicies, other.spicies);

        this->militaryRank = new char[strlen(other.militaryRank) + 1];
        strcpy(this->militaryRank, other.militaryRank);

        this->midiChlorian = other.midiChlorian;
    }


    ~Jedi()
    {
        delete[] this->name;
        delete[] this->rank;

    }
    Jedi& operator=(const Jedi& other)
    {
        if (this != &other)
        {
            delete[] this->name;
            delete[] this->rank;
            delete[] this->spicies;
            delete[] this->militaryRank;

            this->name = new char[strlen(other.name) + 1];
            strcpy(this->name, other.name);

            this->rank = new char[strlen(other.rank) + 1];
            strcpy(this->rank, other.rank);

            this->spicies = new char[strlen(other.spicies) + 1];
            strcpy(this->spicies, other.spicies);

            this->militaryRank = new char[strlen(other.militaryRank) + 1];
            strcpy(this->militaryRank, other.militaryRank);

            this->midiChlorian = other.midiChlorian;
        }
        return *this;

    }

    void printJediInfo()
    {
        cout << this->name << endl;
        cout << this->rank << endl;
        cout << this->spicies << endl;
        cout << this->militaryRank << endl;
        cout << this->midiChlorian << endl;
    }

    void write(ofstream& stream)
    {
        stream << this->name << endl;
        stream << this->rank << endl;
        stream << this->spicies << endl;
        stream << this->militaryRank << endl;
        stream << this->midiChlorian << endl;
    }
};

class Planet {

    char* name;
    char* planetSystem;
    char* republic;

public:

    Planet()
    {
        this->name = nullptr;
        this->planetSystem = nullptr;
        this->republic = nullptr;
    }

    Planet(const Planet &other)
    {
        this->name = new char[strlen(other.name) + 1];
        strcpy(this->name,  other.name);

        this->planetSystem = new char[strlen(other.planetSystem) + 1];
        strcpy(this->planetSystem, other.planetSystem);

        this->republic = new char[strlen(other.republic) + 1];
        strcpy(this->republic, other.republic);
    }


    Planet(const char* name, const char* planetSystem, const char* republic)
    {

        this->name = new char[strlen(name) + 1];
        strcpy(this->name, name);

        this->planetSystem = new char[strlen(planetSystem) + 1];
        strcpy(this->planetSystem, planetSystem);

        this->republic = new char[strlen(republic) + 1];
        strcpy(this->republic, republic);
    }

    Planet& operator=(const Planet& other)
    {
        if (this != &other)
        {
            delete[] this->name;
            delete[] this->planetSystem;
            delete[] this->republic;

            this->name = new char[strlen(other.name) + 1];
            strcpy(this->name,  other.name);

            this->planetSystem = new char[strlen(other.planetSystem) + 1];
            strcpy(this->planetSystem, other.planetSystem);

            this->republic = new char[strlen(other.republic) + 1];
            strcpy(this->republic, other.republic);
        }
        return *this;

    }

    ~Planet()
    {

        delete[]  this->name;
        delete[]  this->planetSystem;
        delete[]  this->republic;

    }


    void PrintPlanet()
    {
        cout << this->name << endl;
        cout << this->planetSystem << endl;
        cout << this->republic << endl;
    }

    void write(ofstream& stream)
    {
        stream << this->name << endl;
        stream << this->planetSystem << endl;
        stream << this->republic << endl;


    }


};

class Stormtrooper {
    char* id;
    char* type;

public:

    Stormtrooper()
    {

        this->id = nullptr;
        this->type = nullptr;

    }


    Stormtrooper(const Stormtrooper& other)
    {

        this->id = new char[strlen(other.id) + 1];
        strcpy(this->id, other.id);

        this->type = new char[strlen(other.type) + 1];
        strcpy(this->type, other.type);

    }

    Stormtrooper(const char* id, const char* type)
    {
        this->id = new char[strlen(id) + 1];
        strcpy(this->id, id);

        this->type = new char[strlen(type) + 1];
        strcpy(this->type, type);
    }

    Stormtrooper& operator=(const Stormtrooper& other)
    {

        if (this != &other)
        {

            delete[] this->id;
            delete[] this->type;


            this->id = new char[strlen(other.id) + 1];
            strcpy(this->id, other.id);

            this->type = new char[strlen(other.type) + 1];
            strcpy(this->type, other.type);

        }
        return *this;
    }

    ~Stormtrooper()
    {

        delete[] this->id;
        delete[] this->type;

    }


    void printSTH()
    {

        cout << this->id << endl;
        cout << this->type << endl;
    }

    void write(ofstream& stream)
    {
        stream << this->id << endl;
        stream << this->type << endl;


    }


};

class JediTemple {
    Jedi* jedi;
    size_t size;
    size_t capacity;

public:
    void copyFrom(const JediTemple& other)
    {
        jedi = new Jedi[other.capacity];

        size = other.size;
        capacity = other.capacity;

        for (int index = 0; index < size; ++index)
        {
            jedi[index] = other.jedi[index];
        }
    }

    void resize()
    {
        capacity *= 2;
        Jedi* j = new Jedi[capacity];

        for (int index = 0; index < size; ++index)
        {
            j[index] = jedi[index];
        }

        delete[] jedi;
        jedi = j;
    }
    JediTemple()
    {
        this->capacity = 5;
        this->size = 0;
        this->jedi = new Jedi[this->capacity];
    }
    JediTemple(const JediTemple& other)
    {
        this->copyFrom(other);
    }

    JediTemple& operator=(const JediTemple& other)
    {
        if (this != &other)
        {
            delete[] this->jedi;
            this->copyFrom(other);
        }

        return *this;
    }
    ~JediTemple()
    {
        delete[] this->jedi;
    }

    void add(const Jedi& j)
    {
        if (size >= capacity) {
            resize();
        }
        jedi[size] = j;
        size += 1;

    }
    void remove()
    {
        this->size--;
    }
    void printJediTemple()
    {
        for (size_t i = 0; i < size; i++)
        {
            jedi[i].printJediInfo();
        }
    }

    void write()
    {
        ofstream of("jedi.txt");
        if (of.is_open())
        {
            for (size_t i = 0; i < size; i++)
            {
                this->jedi[i].write(of);
            }

        }
        of.close();

    }

};

class Army {
    Stormtrooper* stormH;
    size_t size;
    size_t capacity;

public:

    void copyFrom(const Army& other)
    {
        stormH = new Stormtrooper[other.capacity];

        size = other.size;
        capacity = other.capacity;

        for (int index = 0; index < size; ++index)
        {
            stormH[index] = other.stormH[index];
        }
    }

    void resize()
    {
        capacity *= 2;
        Stormtrooper* sth = new Stormtrooper[capacity];

        for (int index = 0; index < size; ++index) {
            sth[index] = stormH[index];
        }

        delete[] stormH;
        stormH = sth;
    }
    Army()
    {
        this->capacity = 10;
        this->size = 0;
        this->stormH = new Stormtrooper[this->capacity];
    }
    Army(const Army& other)
    {
        this->copyFrom(other);
    }
    Army& operator=(const Army& other)
    {
        if (this != &other)
        {
            delete[] this->stormH;
            this->copyFrom(other);
        }

        return *this;
    }
    ~Army()
    {
        delete[] this->stormH;
    }

    void add(const Stormtrooper& sth)
    {
        if (size >= capacity) {
            resize();
        }
        stormH[size] = sth;
        size += 1;

    }

    void remove()
    {
        this->size--;
    }
    void printArmy()
    {
        for (size_t i = 0; i < size; i++)
        {
            stormH[i].printSTH();
        }
    }

    void write()
    {
        ofstream of("Army.txt");
        if (of.is_open())
        {
            for (size_t i = 0; i < size; i++)
            {
                this->stormH[i].write(of);
            }

        }
        of.close();

    }

};

class Galaxy {
private:
    Planet* planet;
    size_t size;
    size_t capacity;

public:
    void copyFrom(const Galaxy& other)
    {
        planet = new Planet[other.capacity];

        size = other.size;
        capacity = other.capacity;

        for (int index = 0; index < size; ++index)
        {
            planet[index] = other.planet[index];
        }
    }

    void resize()
    {
        capacity *= 2;
        Planet* p = new Planet[capacity];

        for (int index = 0; index < size; ++index) {
            p[index] = planet[index];
        }

        delete[] planet;
        planet = p;
    }
    Galaxy()
    {
        this->capacity = 5;
        this->size = 0;
        this->planet = new Planet[this->capacity];
    }
    Galaxy(const Galaxy& other)
    {
        this->copyFrom(other);
    }
    Galaxy& operator=(const Galaxy& other)
    {
        if (this != &other)
        {
            delete[] this->planet;
            this->copyFrom(other);
        }

        return *this;
    }
    ~Galaxy()
    {
        delete[] this->planet;
    }

    void add(const Planet& p)
    {
        if (size >= capacity) {
            resize();
        }
        planet[size] = p;
        size += 1;

    }

    void remove()
    {
        this->size--;
    }
    void printGalaxy()
    {
        for (size_t i = 0; i < size; i++)
        {
            planet[i].PrintPlanet();
        }
    }

    void write()
    {
        ofstream of("Galaxy.txt");
        if (of.is_open())
        {
            for (size_t i = 0; i < size; i++)
            {
                this->planet[i].write(of);
            }

        }
        of.close();

    }



};


int main() {
    Planet one;
    Planet two("AAAA", "bbbbb", "v");
    Planet three(two);
    Planet four = three;

    four.PrintPlanet();


//    four.display();

    cout << "\n----------------Jedi-------------------------\n";
    Jedi j1;
    Jedi j2("ssss", "aaaaa", "dddd", "rrrrrr", 2.5);
    Jedi j3(j2);
    Jedi j4 = j3;

    j4.printJediInfo();


    cout << "\n---------------Storm-----------\n";
    Stormtrooper s1;
    Stormtrooper s2("iddd", "ttttt");
    Stormtrooper s3(s2);
    Stormtrooper s4 = s3;

    s4.printSTH();

    cout << "\n-----------JediTemple------------\n";
    JediTemple temple;
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);
    temple.add(j2);

    JediTemple jt2(temple);
    JediTemple jt3 = temple;

    jt3.write();

    cout << "\n-----------Army------------\n";

    Army army;
    army.add(s2);
    army.add(s2);
    army.add(s2);
    army.add(s2);
    army.add(s2);
    army.add(s2);
    army.add(s2);
    army.add(s2);
    army.add(s2);
    army.add(s2);

    Army a2(army);
    Army a3 = a2;

    a3.write();

    cout << "\n-----------Galaxy------------\n";

    Galaxy galaxy;
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);
    galaxy.add(two);

    galaxy.write();

    Galaxy g2(galaxy);
    Galaxy g3 = g2;

    g3.printGalaxy();


    return 0;
}