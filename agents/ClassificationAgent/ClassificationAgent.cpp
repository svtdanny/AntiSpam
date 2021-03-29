#include <stdio.h>
#include <curl/curl.h>
#include <string.h>

#include <sstream>
#include <iostream>
#include <fstream>

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

    // Open files for debug Output
    std::ofstream req_file;
    req_file.open("/home/antispam/agents/ClassificationAgent/Output.txt");
    std::ofstream log_file;
    log_file.open ("/home/antispam/agents/ClassificationAgent/responses.txt");

    std::string line;
    std::stringstream ss, ssemail, sspost;

    while (std::getline(std::cin, line)) {
        ss << line;
    }

    curl = curl_easy_init();

    if (curl){
        char * encoded_letter = curl_easy_escape(curl, ss.str().c_str(), 0);

        ssemail << argv[1] << "@" << argv[2];
        sspost << "email=" << ssemail.str().c_str() << "&letter=" << encoded_letter;
        
        std::string s = sspost.str();
        
        req_file << sspost.str().c_str() << std::endl;


        struct curl_slist *headers = NULL;
        //headers = curl_slist_append(headers, "Expect:");
        //headers = curl_slist_append(headers, "Content-Type: application/json");
        

        curl_easy_setopt(curl, CURLOPT_BUFFERSIZE, 102400L);
        curl_easy_setopt(curl, CURLOPT_URL, "http://procagent.antispam-msu.site/classificator");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, s.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_USERAGENT, "curl/7.68.0");
        curl_easy_setopt(curl, CURLOPT_MAXREDIRS, 50L);
        curl_easy_setopt(curl, CURLOPT_HTTP_VERSION, (long)CURL_HTTP_VERSION_2TLS);
        curl_easy_setopt(curl, CURLOPT_SSH_KNOWNHOSTS, "/root/.ssh/known_hosts");
        curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "POST");
        curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
        curl_easy_setopt(curl, CURLOPT_FTP_SKIP_PASV_IP, 1L);
        curl_easy_setopt(curl, CURLOPT_TCP_KEEPALIVE, 1L);
        curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 1L);

        
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        res = curl_easy_perform(curl);

        if(res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
        curl_easy_strerror(res));

        if (jsonReader.parse(readBuffer, jsonData)){
            //std::cout << jsonData << std::endl;
            std::cout << jsonData.get("score","") << " "<< jsonData.get("result","") << std::endl;
            log_file << jsonData << std::endl;
        }

        log_file.close();
        req_file.close();

        curl_easy_strerror(res);
        curl_easy_cleanup(curl);
        curl_slist_free_all(headers);    
    }
    
return 0;
}