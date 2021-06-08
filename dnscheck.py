import dns
import dns.resolver

def dnscheck(userinput):
    global type
    global domain

    domain = userinput.split(" ")[0]
    word_list = userinput.split()
    word_count = len(word_list)

    if word_count == 2:
        type = userinput.split(" ")[1]
        output_list = []
        try:
            result = dns.resolver.resolve(domain, type)
            for ipval in result:
                output_list.append(str(type.upper( ) + ": "+ipval.to_text()))
            final_output = ('\n'.join([i for i in output_list[0:]]))
            return final_output

        except dns.resolver.NoAnswer:
            return "No "+ type.upper()+ " record found for "+ domain
        except dns.resolver.NXDOMAIN:
            return "No such domain"
        except dns.rdatatype.UnknownRdatatype:
            return "DNS record type is unknown. Did you check /help ?"

    else:
        return "Looks like an unsupported syntax. Did you check /help ?"
