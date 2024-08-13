#include <xercesc/util/PlatformUtils.hpp>
#include <iostream>
#include <xercesc/dom/DOM.hpp>
#include <xercesc/parsers/XercesDOMParser.hpp>
#include <xercesc/util/XMLString.hpp>
#include <string>

using namespace xercesc;

int main(int argc, char* argv[]) {
	if (argc != 2) {
	std::cerr<<"Usage:" << argv[0] << " <xml_file>" <<std::endl;
	return 1;
	}
	
	const char* xmlFile = argv[1];

	try {
	XMLPlatformUtils::Initialize();
	XercesDOMParser parser;

	XMLCh* xmlFileAsXMLCh = XMLString::transcode(xmlFile);
	parser.parse(xmlFileAsXMLCh);
	DOMDocument* doc = parser.getDocument();
	DOMNodeList* children = doc->getElementsByTagName(XMLString::transcode("title"));
	const XMLSize_t count = children->getLength();
	for (XMLSize_t i = 0; i<count;++i) {
	
		DOMNode* titleNode = children->item(i)->getFirstChild();
	
		if (titleNode && titleNode->getNodeValue()) {
			
			std::string title = XMLString::transcode(titleNode->getNodeValue());
			std::cout << "Book Title: " <<title<<std ::endl;
		}
		
	}
	
	XMLString::release(&xmlFileAsXMLCh);

	XMLPlatformUtils::Terminate();
	} catch (const XMLException& e) {
	std::cerr << "Error Initializing Xerces-C++: "  << std::endl;
return 1;
}
std::cout<<"It worked"<<std::endl;
return 0;
}
