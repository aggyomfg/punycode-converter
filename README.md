
---
International domain names converter.
---

Converts idn both from and to punycode

---
Installation:
---
Clone repository, and copy script to your user bin-dir

    git clone https://github.com/aggyomfg/punycode-converter.git
    cd punycode-converter
    sudo mv ./punycode.py /usr/local/bin/punycode

---
Usage:
---

Examples:

    > punycode http://xn--d1acufc.xn--p1ai/
    домен.рф

    > punycode домен.рф
    xn--d1acufc.xn--p1ai

    > punycode ドメイン.日本
    xn--eckwd4c7c.xn--wgv71a

    > punycode xn--eckwd4c7c.xn--wgv71a
    ドメイン.日本
