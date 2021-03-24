#include <stdio.h>
#include <curl/curl.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <jsoncpp/json/json.h>

// Dependences
//sudo apt-get install libjsoncpp-dev

static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp)
{
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

int main(int argc, char* argv[]){
    CURL *curl;
    CURLcode res;
    std::string readBuffer;
    
    Json::Value jsonData;
    Json::Reader jsonReader;

    //std::cout << "!!!" << std::endl;

    std::string line;
    std::stringstream ss, ssemail, sspost;
    while (std::getline(std::cin, line)) {
        ss << line;
    }
    
    //std::cout << ss.str().c_str() << std::endl;

    ssemail << argv[1] << "@" << argv[2];
    sspost << "{\"email\":\"" << ssemail.str().c_str() << "\", \"letter\":\"" << ss.str().c_str() << "\"}";

    curl = curl_easy_init();
    if (curl){
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");

        curl_easy_setopt(curl, CURLOPT_URL, "http://procagent.antispam-msu.site/classificator");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        curl_easy_setopt(curl, CURLOPT_COPYPOSTFIELDS, sspost.str().c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        res = curl_easy_perform(curl);

        if(res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
        curl_easy_strerror(res));

       

        if (jsonReader.parse(readBuffer, jsonData))
            //std::cout << jsonData.get("message", "no such field: message") << std::endl;
            std::cout << jsonData.get("score","") << " "<< jsonData.get("result","") << std::endl;

        curl_easy_strerror(res);
        curl_easy_cleanup(curl);

        //std::cout << sspost.str().c_str() << std::endl;
    }
    
return 0;

}