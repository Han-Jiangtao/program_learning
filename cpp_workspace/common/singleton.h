#ifndef __SINGLETON_H__
#define __SINGLETON_H__

template <class T>
class Singleton
{
protected:
    Singleton(){};
private:
    Singleton(const Singleton&){};//禁止拷贝
    Singleton& operator=(const Singleton&){};//禁止赋值
    static T* mInstance;
public:
    static T* GetInstance();
};

template <class T>
T* Singleton<T>::GetInstance()
{
    return mInstance;
}

template <class T>
T* Singleton<T>::mInstance = new T();
#endif
