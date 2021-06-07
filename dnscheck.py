import dns
import dns.resolver

records = ("A", "AAAA", "MX", "NS", "PTR", "SOA", "TXT")

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
                output_list.append(str(ipval.to_text()))
            final_output = ('\n'.join([i for i in output_list[0:]]))
            return final_output

        except dns.resolver.NoAnswer:
            return "No AAAA"
        except dns.resolver.NXDOMAIN:
            return "No such domain"
        except dns.rdatatype.UnknownRdatatype:
            return "DNS resource record type is unknown"


    else:
        for rec in records:
            records_list = []
            try:
                result = dns.resolver.resolve(domain, rec)
                for ipval in result:
                    records_list.append(str(rec + ":"+ipval.to_text()))
                #final_output = ('\n'.join(i for i in records_list[0:]))
                #str1 = " "
                #return (str1.join(final_output))
                #for i in records_list:
                #    return i
                print(records_list)

            except dns.resolver.NoAnswer:
                continue
