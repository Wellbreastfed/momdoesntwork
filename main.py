from geocoding_module import Geolocation
import csv

d2_questions = [
    "How is the AC voltage separated from the RF signal in a distribution
    amplifier?",  # 1
    "Describe an application for a distribution amplifier in a hybrid fiber coax network",  # 2
    "What is installed in the input, of a distribution amplifier, for a flat frequency response into the input amplifier when the input signal has a negative tilt?",
    # 3
    "What is a safety concern when aerial fiber-optic cable is installed between poles, even though there are no high-voltage power lines?",
    # 4
    "In which type of optical modulation does the laser operate at a constant output level?",  # 5
    "What is the minimum amount of slack that must be provided for splicing fiber-optic cable in underground installations?",
    # 6
    "What product based on the Data over cable service interface Specification DOCSIS defines protocols for internet Protocol IP Telephony over Hybrid Fiber Coax HFC networks",
    # 7
    "Why was the zero dispersion point in single mode fiber moved to 1550 nm?",  # 8
    "Besides protection, what else must the coating on an optical fiber do?",  # 9
    "Since they provide the same functions, what is the primary difference between the Fiber distribution hub FDH and Fiber access terminal FAT?",
    # 10
    "What can be used as a pulling line in a conduit that is missing a pull line??",  # 11
    "When would a mid entry splice in a fiber optic network be used?",  # 12
    "what is one reason why broadband cable operators install fiber-optic cable in stages instead of changing the infrastructure all at once?",
    # 13
    "Which type of Passive Optical Network(PON) topology places optical splitters at the headend, and then routes them to each individual customer premises?",
    # 14
    "Which type of cable can be used in spans of 3000 feet?",  # 15
    "What is the minimum clearance in the middle of a cable span between the powers secondary conductor and the fiber optic cable belonging to a broadband cable operator?",
    # 16
    "Why are laser diodes most effective when coupled to singlemode fiber?",  # 17
    "Which type of Fiber to the X(FTTH) topology does a passive optical network(PON)use to make  a point-to-multipoint(P2MP) fiber optic cable connection between the broadband cable head end and the customer premises?",
    # 18
    "What are the main elements of an Optical transmitter?",  # 19
    "What information should always be included in fiber-optic network documentation?",  # 20
    "why are backup AC generators included in many commercial AC UPS and DC power systems?",  # 21
    "Which components are used in a passive optical NetworkPON?",  # 22
    "The national Electrical Safety CodeNESC requires drop cables to be placed at what minimum depth?",  # 23
    "What is true about using a premade fiber optic pigtail for splicing to patch panels or terminal equipment?",  # 24
    "What function does the detector in an optical receiver perform?",  # 25
    "What is the purpose of a MST?",  # 26
    "What are the two critical elements that align the optical fibers in a connection?",  # 27
    "What is a drawback of using Fabry-Perot (F-P)lasers in high-speed data (HSD) networks?",  # 28
    "Which fusion splicer alignment method uses a camera to align the optical fibers before splicing?",  # 29
    "Why are backup AC generators included in many commercial AC UPS and DC power systems?",  # 30
    "Which statement about pigtails used for fiber terminations is true?",  # 31
    "Why is -48 VDC with a positive ground used by the telecommunications industry?",  # 32
    "What is the purpose of splice trays inside splice closures?",  # 33
    "Digital return path transmissions?",  # 34
    "What are some prerequisites before performing a fusion splice of optical fibers?",  # 35
    "Where would a mid-entry splice in a fiber-optic network be used?",  # 36
    "What is the total direct current (DC) loop resistance of a 350-foot piece of series 59 drop cable when the DC loop resistance of that series 59 cable is 56.04 ohms per 1,000 feet??",
    # 37
    "Which form of fluctuating DC is a symptom of a malfunctioning DC power supply in HFC amplifiers and fiber nodes??",
    # 38
    "What occurs in the wavelength division multiplexing process?",  # 39
    "Where are upstream levels and sweep responses measured in a HFC network??",  # 40
    "Which type of network topology allows troubleshooting a problem or switching around the problem to be accomplished easily from the central hub?",
    # 41
    "What is one reason why broadband cable operators install fiber-optic cable in stages instead of changing the infrastructure all at once?",
    # 42
    "Which type of star topology used in a PON places the PON splitters into fiber access terminal (FAT) located deep in the network and closer to the customer premises than the centralized split?",
    # 43
    "What system is a byproduct of the 'funneling effect'?",  # 44
    "Pigtails are coated to...",  # 45
    "Internet protocol telephony systems in broadband cable networks",  # 46
    "What is the core objective of the Data Over Cable Service Interface Specification (DOCSIS) Provisioning of Ethernet passive optical network (EPON), or DPoE, access architecture",
    # 47
    "What is the wavelength allocation for video distribution (RF overlay) in broadband PON (BPON) access systems",
    # 48
    "Which type of optical detection involves a photodiode that converts the light waves to an electrical signal that varies in proportion to intensity changes in the light waves",
    # 49
    "Pig tails should be",  # 50
]
#D2------------------------------------------------------------------D2#
d2_options = [
    [
        "A. By a capacitor that passes RF but blocks the low frequency 60 hertz(Hz) AC voltage which finds a low resistance path through the RF choke that blocks RF",
        # 1
        "B. By incorporating a large bypass filter into the network for other technicians to use",
        "C. The headend filters the AC voltage with a splice block and attenuator.",
        "D. By using a AC voltage seperated"],
    ["A. Star topology",
     "B. Incorporating head end technologies",
     "C. By using a node 4x4 in a FTTx network",
     "D. To maintain downstream amplitude levels to the adresses farthest from the fiber-node."],  # 2
    ["A. A fiber equalizer with a positive slope",
     "B. A cable equalizer with a positive slope",  # 3
     "C. A cable equalizer with a negative slope",
     "D. A Fiber equalizer with a negative slope"],
    ["A. hamrful light energy could be emitted from the cable affecting aircraft pilows",
     "B. the buildup of lethal amounts of static electricity on the fiber-optic cable that can be discharge through a person on a ladder or some other conductor to ground.",
     # 4
     "C. During high wind, the fiber-optic cable will begin to swing",
     "D. the weight of the fiber-optic cable could pull the poles down"],
    ["A. indirect modulation",  # 5
     "B. light fiber",
     "C. constant on button switch by the node amplifier",
     "D. Direct modulation"],
    ["A. 5 meters on both the inbound and outbound span",
     "B. 50 meters on both the inbound and outbound span",
     "C. 15 meters on both the inbound and outbound span",  # 6
     "D. 1000 meters on both the inbound and outbound span"],
    ["A. Fiber-optic cable",
     "B. Headend cable",
     "C. Packetcable",  # 7
     "D. distribution cable."],
    ["A. To take advantage of the low intrinsic absorption and lower attenuation at 700nm single-mode fiber.",
     "B. To take advantage of the low intrinsic absorption and lower attenuation at 15nm single-mode fiber.",
     "C. To take advantage of the low intrinsic absorption and lower attenuation at 50nm single-mode fiber.",
     "D. To take advantage of the low intrinsic absorption and lower attenuation at 1550nm single-mode fiber."],  # 8
    [
        "A.  Function over a wide temperature range, be compatible with cable gels, adhere to the glass cladding over the lifetime of the cable, and be mechanically strippable for splicing operations",
        # 9
        "B. To take advantage of the high intrinsic absorption and higher attenuation at 1550 nm in single-mode fiber",
        "C. Loose tube buffer cable",
        "D. The ITU-T G.657 bend-insensitive fiber (BIF) radius squared over time"],
    [
        "A. Function over a wide temperature range, Emit head, adhere to the glass cladding over the lifetime of the cable, and be mechanically strippable for splicing operations.",
        "B. Emit heat",
        "C. maintain a constant output at the network node",
        "D. The FAT is typically easier to install and has lower fiber counts than the FDH.."],  # 10
    ["A. The mitochondria is the powerhouse of the cell",
     "B. An unused cable that is already installed in the conduit..",  # 11
     "C. access to a different splice enclosure",
     "D. Fiber pigtails, color coded and strippable so technicians have easy access"],
    ["A.  That is based on the designer",
     "B.  That is based on the construction coordinator",
     "C.  In a self healing ring network that requires only two fibers to feed an optical fiber drop.",  # 12
     "D.  In a self healing STAR network that requires only two fibers to feed an optical fiber drop.n"],
    ["A. changing the infrastructure all at once would create excessive network congestion",
     "B. changing the infrastructure all at once would cause too many service disruptions",  # 13
     "C. changing the infrastructure all at once would require too many new drops to be created",
     "D. changing the infrastructure all at once would put a strain on equipment manufacturers"],
    ["A. Star-Bus",
     "B. Distributed Star",
     "C. Home-Run",  # 14
     "D. point-to-point"],
    ["A. fiber",  # 15
     "B. Cat9",
     "C. Charter doesnt do 3000 feet spans",
     "D. cat7"],
    ["A. 15 inches",
     "B. 25 inches",
     "C. 3 feet",
     "D. 30 inches"],  # 16
    ["A. Its high coupled power, directionality, and speed.",  # 17
     "B. its high cost and low fiber count",
     "C. its low cost and high fiber count",
     "D. Its low cost,high fiber count and speed."],
    ["A. FIBER-TO-THE-HOME",  # 18
     "B. FIBER-TO-THE-PREMISES",
     "C. FIBER-TO-THE-HUB",
     "D. FIBER-TO-THE-NODE"],
    ["A. Demodulator, electrical interface, optical detector, optical interface.",
     "B. Data encoder/modulator, electrical interface, laser, optical interface",  # 19
     "C. back up power supply, electrical interface, laser, optical interface",
     "D. laser sight, electrical interface, laser, optical interface"],
    ["A. utility power supplies and plugs for seperate electrical equipment",
     "B. emergency restoration services",
     "C. fiber assignments",  # 20
     "D. address access codes"],
    ["A. to charge the UPS batteries in the event of a prolonged utility power interruption",
     "B. to boost the voltage provided by the UPS",
     "C. to act as a bufer between commercial power and the UPS",
     "D. To provide AC power in the event of a prolonged utlity power interruption."],  # 21
    ["A. utility discharge cable",
     "B. optical epons, optical splitters AND utility discharge cable ",
     "C. optical EPONS",
     "D. optical splitters"],  # 22
    ["A. 3 yards",
     "B. 18 feet",
     "C. 1 foot",
     "D. 18 inches"],  # 23
    ["A. theyre a general use product for cable manufacturers",
     "B. they require LC connectors",
     "C. it is safer from break or lightning damage",
     "D. it is faster and more reliable than installing connectors in the field."],  # 24
    ["A. Conversion of a coaxial signal inputted to a node, and outputted to a fiber signal",
     "B. Conversion of an optical carrier to an electrical signal, and demodulation of the modulated optical carrier.",
     # 25
     "C. An optical node converts a modular signal to a patch panel design in a coaxial bidirectional signal.",
     "D. The mitochondria is the powerhouse of the cell"],
    ["A. it provides access to fiber-optic cable drops from the customer premises to the network",  # 26
     "B. it is located just after the fiber node to allow special services to be deployed",
     "C. it is required on large fiber counts to split the network",
     "D. it provides a special splice tray for optical splitters"],
    ["A. conductor and conductance plate",
     "B. LC connector panel and fiber light identifier",
     "C. the ferrules and the mating adapter.",  # 27
     "D. semiconductor wall and DC output to RF entry modulator"],
    ["A.  Star plenum cable bundles.",
     "B. The emission of a number of discrete wavelengths or side modes.",  # 28
     "C. a Nm detector",
     "D. Coaxial power supply modulators"],
    ["A. PDSU method through a fiber identifier",
     "B. The profile alignment system (PAS) method.",  # 29
     "C. WDM-PON deployed in a greenfield system that allows each subscriber to get their own designated wavelength",
     "D. Trunk, branch, drop"],
    ["A. To provide DC power in the event of a prolonged utility power interruption. ",
     "B. To provide RF power in the event of a prolonged utility power interruption. ",
     "C. To provide AC power in the event of a prolonged utility power interruption. ",  # 30
     "D. To provide VDC power in the event of a prolonged utility power interruption. "],
    [
        "A. AFTER to splicing, pigtails should be labeled to correspond with the correct color code and patch panel designatioN",
        #
        "B. prior to splicing, pigtails should be labeled to correspond with the correct color code and patch panel designation.",
        # 31
        "C. before or after splicing, pigtails should be labeled to correspond with the correct color code and patch panel designation.",
        "D. during splicing, pigtails should be labeled to correspond with the correct color code and patch panel designation."],
    ["A. This reverse polarity is a means of mitigating electrolytic corrosion on the outside plant.",  # 32
     "B. This bidirectional polarity is a means of mitigating electrolytic corrosion on the outside plant.",
     "C. This reverse segmented polarity is a means of mitigating electrolytic corrosion on the outside plant.",
     "D. This semidirectional polarity is a means of mitigating electrolytic corrosion on the outside plant."],
    ["A. involves the use of a node transponder that continuously monitors a number of critical functions",
     "B. Splice trays are designed to provide protection for mechanical splices, fusion splice protectors, and optical splitters as well as provide storage for the required fiber slack.",
     # 33
     "C. The larger the MFD, the easier it is to splice and connectorize the fiber, although it becomes more sensitive to bending losses.",
     "D. By using a compressed-air cleaner designed for optical connectors"],
    ["A. access fiber nodes over QAM modulators into hub-to-headend architectures",
     "B. Hub and spoke fiber topologies",
     "C. use dense wavelength division multiplexing (DWDM) digital return transmitters in hub-to-headend architectures",
     # 34
     "D. rim and spoke fiber topologies"],
    ["A. A mobilezed bucket truck with safety tools",
     "B. sealed zip lock bags and construction zip ties for water resistance",
     "C. There are no prerequisites, fiber is a redundant technology",
     "D. A controlled environment such as a splicing van, trailer, or tent and a stable work surface that is large enough to accommodate the fusion splicer, tools , and the splice closure."],
    # 35
    ["A. In a self healing ring network that requires only two fibers to feed an optical fiber drop.",  # 36
     "B. In a self healing ring network that requires only one fibers to feed an optical fiber drop.",
     "C. In a self healing ring network that requires only three fibers to feed an optical fiber drop.",
     "D. In a self healing ring network that requires only four fibers to feed an optical fiber drop."],
    ["A. 1 ohm x 2nm/ 4nm = x",
     "B. 7 ohms",
     "C. 19.614 ohms",  # 37
     "D. 12 ohms"],
    ["A. VDC RIPPLE",
     "B. DR RIPPLE",
     "C. AC RIPPLE",  # 38
     "D. RF RIPPLE"],
    [
        "A. The optical output from a single laser operating at different wavelengths is combined and transported over a single, common optical fiber.",
        "B. The optical output from multiple lasers operating at different wavelengths is combined and transported over a single, common optical fiber.",
        # 39
        "C. The optical output from bidirectional lasers operating at different wavelengths is combined and transported over a single, common optical fiber.",
        "D. The optical output from  a single coaxial trunk operating at different wavelengths is combined and transported over a single, common optical fiber."],
    ["A. DC8s, DC12s, AND DC16s",
     "B. THE TAP",
     "C. THE NODE",
     "D. THE HEADEND"],  # 40
    ["A. anais topology",
     "B. bus",
     "C. star",  # 41
     "D. local"],
    ["A. Changing the infrastructure all at once would cause too many service disruptions.",  # 42
     "B. Noise. It is more redundant to take our time.",
     "C. We only design one network at a time.",
     "D. the FDIC and NIST communications regulate our methods."],
    ["A. star",
     "B. Distributed star",  # 43
     "C. home-run",
     "D. anais topology"],
    ["A. a many to none system",
     "B. outages and noise",
     "C. a circuit system",
     "D. a many to one system."],  # 44
    ["A. 100m diameter/30um tolerance",
     "B. 600m diameter/30um tolerance",
     "C. 700m diameter/30um tolerance",
     "D. 900m diameter/30um tolerance"],  # 45
    ["A. Require a node medium, circuit switch, signaling gateway, billing system, and CMTS.",
     "B. Require a call management server, media gateway, signaling gateway, billing system, and CMTS.",  # 46
     "C. Require a node medium, media gateway, signaling gateway, billing system, and CMTS.",
     "D. Require a circuit switch, media gateway, signaling gateway, billing system, and CMTS."],
    ["A. To use return path operations for legible fiber optic light transmission",
     "B. To make the EPON elements appear and operate as DOCSIS elements to the existing DOCSIS-based back office provisioning operations.",
     # 47
     "C. GPONS communicate with fiber nodes over coaxial signals for return path transmssions",
     "D. DPOE's call a circuit switch network to RFOGs over customer networks"],
    ["A. between 1,550 and 1,560 nm",  # 48
     "B. between 1,490 and 1,760 nm",
     "C. between 1,550 and 1,460 nm",
     "D. between 1,550 and 1,660 nm"],
    ["A. DIRECT",  # 49
     "B. INDIRECT",
     "C. BIDIRECTIONAL",
     "D. MODULAR"],
    ["A. uploaded to prism ",
     "B. visible in magellan",
     "C. Labeled and documented",  # 50
     "D. visible in prism and magellan"],
]
#OPTIONS------------------------------------------------------------------OPTIONS#
d2_correct_answers = ["A", "D", "B", "B", "A", "C", "C", "D", "A", "D", "B", "C", "B", "b", "A", "D", "A", "A", "B",
                      "C", "D", "D", "D", "D", "B", "A", "C", "B", "B", "C", "B", "A", "B", "C", "D", "A", "C", "C",
                      "B", "D", "C", "A", "B", "D", "D", "B", "B", "A", "A", "D"]  # Specify the correct answers here
#CORRECT------------------------------------------------------------------ANSWERS#
d3_questions = [
    "What topology do most fiber-to-the-user (FTTx) networks use, which requires greater fiver color code management in its documentation?",
    # 1
    "During installation of fiber-optic cable, what does damage to the cable jacket cause?",  # 2
    "In a fiber-optic network,",  # 3
    "A fiber-optic network maintenance plan should be developed with which of the following in mind?",  # 4
    "When testing the fiber-optic plant,",  # 5
    "Definition of Point-to-multipoint (P2MP)",  # 6
    "Optoelectronics",  # 7
    "Patch Panel",  # 8
    "Microbend",  # 9
    "Optical power meters used for testing fiber-to-the-user (FTTx) installations operating downstream from the headend should be calibrated for which wavelengths?",
    # 10
    "A wavelength-isolating power meter is most commonly used in",  # 11
    "Optical loss test sets perform multiple functions because they include the features of multiple pieces of test sets. The features of which other test sets are combined into an optical loss test set?",
    # 12
    "Regarding various optical power meter types,",  # 13
    "When measuring transmit and receive power with an optical power meter,",  # 14
    "When measuring end-to-end attenuation,",  # 15
    "A light source",  # 16
    "When a laser light source is used to test fibers,",  # 17
    "Optical fiber identifiers",  # 18
    "Which of the following describe optical time domain reflectometer (OTDR) nonreflective signatures?",  # 19
    "The most common single-mode wavelengths used by OTDRs are:",  # 20
    "What is unique to a fiber break locator?",  # 21
    "Full-feature OTDRs, also known as platform OTDRs, have these as options:",  # 22
    "Regarding reflections in an optical fiber,",  # 23
    "What is true of mainframe optical time domain reflectometers (OTDR)?",  # 24
    "What do OTDR displays and controls encompass?",  # 25
    "What is the probable cause if an OTDR trace shows one optical splice but it is a known fact that there are two?",
    # 26
    "Optical return loss (ORL) is used to define the amount of reflection from",  # 27
    "Which wavelength is the most sensitive to macrobends and microbends and has been specified by standards groups for testing and monitoring of fiber-optic spans?",
    # 28
    "When programming an optical time domain reflectometer (OTDR),",  # 29
    "In optical time domain reflectometer (OTDR) terminology,",  # 30
    "The optical fiber acceptance test",  # 31
    "What is the result of increasing (making wider or longer) the pulse width on an optical time domain reflectometer (OTDR)?",
    # 32
    "What is the best course of action for the optical time domain reflectometer (OTDR) operator when the distance measurement for a strand of fiber doesn't match the sequential distance markings on the outside of the cable jacket?",
    # 33
    "What is the difference between a reflectance measurement and an optical return loss (ORL) measurement with an optical time domain reflectometer (OTDR)?",
    # 34
    "When cleaning the optical port of an optical time domain reflectometer (OTDR), which connector port requires the use of a 1.25 mm swab?",
    # 35
    "When using mechanical splices and other connection techniques on bare optical fibers,",  # 36
    "Optical time domain reflectometer (OTDR) signatures",  # 37
    "When performing an optical fiber acceptance test,",  # 38
    "Choosing the appropriate optical measurement for post-installation fiber-optic span tests",  # 39
    "When testing a fiber-optic splitter with an optical time domain reflectometer (OTDR), what would cause all the splitter output ports to look the same on the OTDR's display?",
    # 40
    "What are possible causes of a nonreflective OTDR trace signature?",  # 41
    "How can an optical time domain reflectometer (OTDR) operator compare an old fiber trace with a new one?",  # 42
    "What does the laser array diagram show?",  # 43
    "Additional optical attenuation",  # 44
    "Digital channel signal testing",  # 45
    "Fiber-optic power meters used in fiber-to-the-home (FTTH) networks should be able to measure which of the following two additional wavelengths?",
    # 46
    "What do optical power meters measure?",  # 47
    "What is an optical return loss test set used for?",  # 48
    "Choosing the appropriate optical measurement for post-installation fiber-optic span tests",  # 49
    "What criteria should be met when setting up the optical return path?",  # 50

    ]  # List of d3 test questions
#QUESTIONS------------------------------------------------------------------QUESTIONS#
d3_options = [
    ["A.peak value",
     "B.The amplifier AC circuitry.",
     "C. Point-to-multipoint (P2MP).",  # 1
     "D.The battery-powered inverter.  "],
    ["A. Using two parallel metal plates separated by an insulator.",
     "B.,Capacitors in parallel act like one large capacitor",
     "C.,The amplifier AC circuitry.",
     "D. Moisture migration into the cable."],  # 2
    ["A. Because the capacitive and inductive reactance vary with the AC frequency.",
     "B.the quality factor (Q).",
     "C. The role of maintenance is to proactively maintain network tolerances and recognize, locate, and remedy potential problems.",
     # 3
     "D.Group delay."],
    [
        "A.The task of compiling the physical document must become the responsibility of an identifiable position or organization. ",
        # 4
        "B.an automatic gain control",
        "C.the higher the temperature, the greater the cable attenuation.",
        "D.make sure cover plates are tightend"],
    [
        "A. An optical power meter is used to measure the strength of light signals anywhere in a fiber system where a connection can be made",
        # 5
        "B.Allows the designer to place amplifiers without concern about access to electrical utility power.",
        "C.Baseline sweep responses that are used to balance and sweep all the amplifiers serviced by that fiber-node.",
        "D.To select equalizers and set the output amplitude levels."],
    ["A.How much equalization is being applied to the channel. ",
     "B.Applications that have small random noise-like errors.",
     "C.The data rates of the compressed content and the data rate capacity of the QAM channel.",
     "D.A network topology that specifies a direct connection from a central or common location to multiple network locations."],
    # 6
    [
        "A. Because Velcro straps are removable and can hold the pigtails together without placing undue strain on the optical fibers",
        "B.Leave enough slack in the buffer tubes to allow the splice trays to reach the splicing equipment and enough fiber slack to store on individual trays for later additions, moves and changes",
        "C. Any technology that responds to light waves or is used in a fiber plant, such as a laser, photodiode, optical coupler or amplifier, etc.",
        # 7
        "D.The distribution panel can be located anywhere in the facility since the distribution cable complies with indoor code requirements for riser or plenum installations."],
    [
        "A.Make a number of test splices to set up the fusion splicer and to verify the instrument's settings and calibration for both the environment and the type of fiber to be spliced. ",
        "B.Consideration of how and who will provide AC power to the optical network terminal (ONT) at the customer premisis",
        "C.Also known as a connector panel, uses interconnection sleeves mounted on a panel, which accommodates an individual optical fiber connection on one side and an equipment connection on the other side.",
        # 8
        "D.an atenuator pad"],
    ["A. When the source and wire resistances are very small.",
     "B. Small imperfections in the core/cladding boundary of a fiber that attenuate the optical signal.",  # 9
     "C.The offline type routes incoming power directly to connected devices and switches to battery backup during a power interruption",
     "D.The reverse polarity is a means of mitigating electrolytic corrosion on the outside plant."],
    ["A1,490 nm, 1,560 nm, and 1,567 nm",
     "B.1,490 nm, 1,550 nm, and 1,577 nm.",  # 10
     "C1,550 nm, 1,665 nm, and 2477 nm.",
     "D.1,490 nm, 1,550 nm, and 1,577 nm"],
    ["APoint-to-multipoint FTTo installations",
     "B.Point-to-multipoint FTTy installations",
     "C.Point-to-multipoint FTTh installations",
     "D. Point-to-multipoint FTTx installations."],  # 11
    ["A.The fixed V-Groove splicer. ",
     "B.A stabilized light source, an optical return loss meter, an enhanced optical power meter, and an optical talk set.",
     # 12
     "C.A mechanical splice used for acceptance testing should be simple to use and reusable.",
     "D.In a self-healing ring network that requires only two fibers to feed an optical fiber drop."],
    [
        "A. Enhanced power meters evolved for roles where measurements need to be easily stored, recalled, transmitted, and downloaded.",
        # 13
        "B.It can provide sufficient power for a fiber-optic node, including outside plant amplifiers and customer premises network interface devices (NID) for telephony service. ",
        "C. STB and DOCSIS modems are assigned different upstream channels with dedicated receivers in the headend.",
        "D.The upper edge of the sub-band is prone to group delay cause by the diplex filters."],
    ["A. 2 amperes and 50,000 volts.",
     "B.The meter's calibration must be traceable to the National Institute of Standards Technology (NIST).",  # 14
     "C.The time that it takes for completion, of one cycle of the signal",
     "D.The quasi-square wave edges become more rounded"],
    ["A. With energy that is temporarily stored in an electric field.",
     "B.The light source and optical power meter must be referenced together prior to making any field measurement.",
     # 15
     "C.Capacitors in parallel act like one large capacitor",
     "D.With an AC source, the capacitor continuously charges and discharges for current flow in the same direction, appearing to pass through the capacitor."],
    ["A. With energy that is temporarily stored in an electric field.",
     "B.Is crucial for accurately measuring optical fiber power and attenuation",  # 16
     "C.The band of frequencies between the 70.7% points of the voltage curve for parallel resonant circuits or the current curve for series resonant circuits.",
     "D.The quality factor (Q)."],
    [
        "A.A 2 kHz modulation provides a test signal that allows the fiber under test to be detected by an optical fiber identifier.",
        # 17
        "B.Because the capacitive and inductive reactance vary with the AC frequency.",
        "C.Band-stop filters.",
        "D.The higher the frequency, the higher the inductive reactance."],
    ["A. The current in the secondary windings must step down in proportion to the voltage increase.",
     "B.By passing voltage surges to ground without damage.",
     "C. Detect live traffic signals or modulated test signals on an individual optical fiber.",  # 18
     "D.To prevent the 60 hertz (Hz) alternating current (AC) from passing between the two radio frequency (RF)/AC ports."],
    ["A. Allows the designer to place amplifiers without concern about access to electrical utility power.",
     "B.In a path common to the downstream and upstream.",
     "C.Baseline sweep responses that are used to balance and sweep all the amplifiers serviced by that fiber-node.",
     "D.Fusion splices, macrobends, and microbends."],  # 19
    ["A.1,310 nm and 1,550 nm",  # 20
     "B.The approximate distance from the test point to the fault.",
     "C.When of equal amplitude and bandwidth, the power level of a QAM channel is several decibel (dB) higher than an analog TV channel.",
     "D.How close the QAM channel is to the cliff where the number of bit errors exceeds the forward error correction (FEC) capacity of the receiver and reception stops."],
    ["A. How much equalization is being applied to the channel.",
     "B.The upstream channels from the built-in DOCSIS modem are optimized for the upstream path and the channel parameters displayed by the instrument.",
     "C.It is the least expensive type of OTDR.",  # 21
     "D.The screens use initials, acronyms, and jargon intended for people that are familiar with the product."],
    ["A. When the source and wire resistances are very small.",
     "B.All power from the primary is transferred to the secondary",
     "C.to route the forward and return signals",
     "D.Chromatic dispersion and polarization mode dispersion (PMD) module interfaces."],  # 22
    ["A.frequency division multiplexing",
     "B.Rayleigh scattering is caused by compositional fluctuations or core imperfections in the fiber.",  # 23
     "C.STB and DOCSIS modems are assigned different upstream channels with dedicated receivers in the headend.",
     "D.The narrow bandwidth and QPSK Quadrature phase shift keying modulation."],
    ["A.The upper edge of the sub-band frequency spectrum is prone to group delay caused by the diplex filters.",
     "B.For situations when long service drops are used and the forward path needs to be amplified but return path amplifiaction is unneccessary.",
     "C.They are used mainly in the fiber manufacturing industry.",  # 24
     "D.To compensate for variable amounts of attenuation in the return path of each device."],
    [
        "A. To route the forward and return signals over different circuit paths to the appropriate section so that they can be amplified separately.",
        "B.Impulse noise will appear as random spikes of energy across the entire return path frequency spectrum (5 to 42 MHz).",
        "C.By ensuring that the RF input is at or above the specified minimum input level to all amplifiers.",
        "D. Ask options, which include range, pulse width, wavelength, measuring mode, backscatter coefficient, and index of refraction."],
    # 25
    ["A.The pulse width is set too long.",  # 26
     "B.In micro-reflections, the echoed signals arrive back at the source with a time delay relative to the incident",
     "C.Regardless of the frequency, if the impulse noise or ingress is high enough, it can cause laser clipping.",
     "D.That there are high micro-reflections and that the cause is near the modem, likely in the drop system."],
    ["A.The amount of light entering the receiver reflected off the last connection in the span. ",  # 27
     "B.Prescreening the drop system for ingress or egress",
     "C.MPEG-1.(MPEG-1 Is the most basic of the audio/video application MPEG. Should be easy to remember)",
     "D.Transport of digital TV (DTV) content over error-free media for recording and play-back or copied and pasted into computer file folders.(page 466)"],
    ["A. The 1,625 nm wavelength is the most sensitive wavelength for micro- and macrobend detection.",  # 28
     "B.The data rates of the compressed content and the data rate capacity of the QAM channel.",
     "C.Focus less on the capacitance, and more on the resistor. As the resistor, once teamed with the capacitance, only then has the POWAH to block RF/radio noise",
     "D.In micro-reflections, the echoed signals arrive back at the source with a time delay"],
    ["A.The signal power sent to the tap port is not available to go to the output port ",
     "B.the higher the temperature, the greater the cable attenuation.",
     "C. Configuration settings include index of refraction (IOR), pulse width, range, wavelength, dead zone, event dead zone, masking, noise floor, and loss variables.",
     # 29
     "D.make sure cover plates are tightend"],
    [
        "A. The distribution panel can be located anywhere in the facility since the distribution cable complies with indoor code requirements for riser or plenum installations.",
        "B.The quality and attenuation value of the mechanical splice of optical fibers is dependent on the quality of the cleaving tool.",
        "C.Acceptance testing consists of checking two-point attenuation, the index of refraction vs. the actual cable length, and zooming in to correctly place markers.",
        # 30
        "D.Because Velcro straps are removable and can hold the pigtails together without placing undue strain on the optical fibers"],
    [
        "A.Make a number of test splices to set up the fusion splicer and to verify the instrument's settings and calibration for both the environment and the type of fiber to be spliced. ",
        "B.the offline type routes incoming power directly to connected devices and switches to battery backup during a power interruption",
        "C.The reverse polarity is a means of mitigating electrolytic corrosion on the outside plant.",
        "D.Is the best opportunity to adjust the fiber's index of refraction (IOR) to match the sequential markings of the cable jacket prior to installation."],
    # 31
    ["A. Common voltages produced by DC power supplies include +5, +12, and +24VDC",
     "B.The OTDR's range increases and its ability to distinguish closely spaced events decreases.",  # 32
     "C.STB and DOCSIS modems are assigned different upstream channels with dedicated receivers in the headend.",
     "D.The upper edge of the sub-band is prone to group delay cause by the diplex filters."],
    [
        "A. Adjust the index of refraction (IOR) settings on the OTDR until the measured distance matches the sequential distance markings",
        # 33
        "B.For situations when long service drops are used",
        "C.At sub-band frequincies, the signal attenuation is significantly less than in the forward path.",
        "D.It is often best accomplished by simulating a fiber-optic cable failure."],
    [
        "A. A reflectance measurement measures an individual component and an ORL measurement measures the sum of all components.",
        # 34
        "B.All the power drawn from the source by the primary circuit is transferred to the secondary circuit.",
        "C.The voltage levels can vary depending on the number of amplifiers powered through the distribution amplifier ports.",
        "D.Rough balanced amplifiers have large gaps of unobserved spectrum that could have frequency response related issues."],
    ["A. Through a power cable that is connected from the power supply directly to the power port of the node.",
     "B.At the output of a forward amplifier because the forward levels are highest and the return levels are lowest",
     "C.The resource manager re-packetizes the data into a new transport stream.",
     "D. Lucent connector (LC)."],  # 35
    ["A. The quasi-square wave edges become more rounded",
     "B.In some cases, the bare optical fiber can be indirectly connected to the optical time domain reflectometer (OTDR) using a system jumper, interconnection sleeve, and a bare fiber adapter.",
     # 36
     "C.Rough balanced amplifiers have large gaps of unobserved spectrum that could have frequency response related issues.",
     "D.The distance in degrees from the 0° reference point to any other point on the waveform.(Remember a wave starts from 0 in the Telecom industry.)"],
    ["A.Allows the designer to place amplifiers without concern about access to electrical utility power.",
     "B.Battery care.",
     "C.Include reflective, nonreflective, gain, roll-off, and ghost types.",  # 37
     "D.Narrow-band continuous wave (CW) test carriers, called pulses, at frequencies between channels."],
    ["A. Organize the fibers by color, per the TIA-598-A standard.",  # 38
     "B.The plate connected to the positive battery terminal becomes positively charged as electrons, attracted by the positive voltage, flow from the plate.",
     "C.Approximately 63% of the source voltage",
     "D.With an AC source, the capacitor continuously charges and discharges for current flow in the same direction, appearing to pass through the capacitor."],
    ["A. Because the capacitive and inductive reactance vary with the AC frequency.",
     "B.An opposing voltage called counter electromagnetic force (cemf) that is proportional to the rate of the changing current.",
     "C.To conduct a site visit to verify the extent of the damage.",
     "D.Includes splice loss, attenuation measurements of fiber segments, component reflectance, optical splitters, accumulated loss, dual wavelength testing, bi-directional testing, and pass/fail analysis."],
    # 39
    ["A. The amplifier AC circuitry.",
     "B.An equal percentage fiber-optic splitter with all the same drop lengths.",  # 40
     "C.To prevent the 60 hertz (Hz) alternating current (AC) from passing between the two radio frequency (RF)/AC ports.",
     "D.3.0 dB peak-to-valley (P/V)."],
    ["A. Sweep test pulse amplitude.",
     "B.Fusion splices, macrobends, microbends, and fused biconical taper (FBT) splitters.",  # 41
     "C. Slope and response variations of the headend and optical transport.",
     "D.A loose seizure screw in the downstream path."],
    ["A.Overlaying a new trace on top of a previously saved trace.",  # 42
     "B.The approximate distance from the test point to the fault.",
     "C.To select equalizers and set the output amplitude levels.",
     "D.How close the QAM channel is to the cliff where the number of bit errors exceeds the forward error correction (FEC) capacity of the receiver and reception stops."],
    ["A. It is based on modulating an analog RF carrier with digital data.",
     "B.The number of optical transmitters, splitters, couplers, and receivers in the headend.",  # 43
     "C.How much equalization is being applied to the channel.",
     "D.The screens use initials, acronyms, and jargon intended for people that are familiar with the product."],
    [
        "A. The upstream channels from the built-in DOCSIS modem are optimized for the upstream path and the channel parameters displayed by the instrument.",
        "B.Coherent interference from ingress, or a beat from another channel modulator, landing inside the QAM channel.",
        "C.Can be obtained by use of an in-line optical attenuator. Some manufacturers provide a front panel interface allowing the user to add or remove optical attenuation.",
        # 44
        "D.STB and DOCSIS modems are assigned different upstream channels with dedicated receivers in the headend."],
    [
        "A. Should be performed in both the downstream and upstream paths and should include bit error rate and modulation error rate performance measurements.",
        # 45
        "B.The upper edge of the sub-band frequency spectrum is prone to group delay caused by the diplex filters.",
        "C.Task options, which include range, pulse width, wavelength, measuring mode, backscatter coefficient, and index of refraction..",
        "D.Prescreening the drop system for ingress or egress"],
    ["A. Transport of MPEG-2 data on low-modulation level data streams.",
     "B.The data rates of the compressed content and the data rate capacity of the QAM channel.",
     "C.1,490 nm and 1,625 nm",  # 46
     "D.The optical output power of the laser transmitter and the input optical power level at the receiver."],
    [
        "A.Of the input on most optical receivers used in the broadband cable industry is accomplished by including a DC voltage test point. ",
        "B.Measuring the amount of reflected energy from the fiber's internal Rayleigh scattering and Fresnel reflections.",
        "C.For situations when long service drops are used and the forward path needs to be amplified but return path amplifiaction is unneccessary.",
        "D.The optical output power of the laser transmitter and the input optical power level at the receiver."],
    # 47
    [
        "A. To route the forward and return signals over different circuit paths to the appropriate section so that they can be amplified separately.",
        "B.Measuring the amount of reflected energy from the fiber's internal Rayleigh scattering and Fresnel reflections.",
        # 48
        "C.By ensuring that the RF input is at or above the specified minimum input level to all amplifiers.",
        "D.Of the input on most optical receivers used in the broadband cable industry is accomplished by including a DC voltage test point."],
    ["A. At the output of a forward amplifier because the forward levels are highest and the return levels are lowest.",
     "B.In micro-reflections, the echoed signals arrive back at the source with a time delay relative to the incident",
     "C.First, the technician at the receiver location (headend) should measure and document the optical input power level (measured in dBm) using a power meter.",
     "D.ncludes splice loss, attenuation measurements of fiber segments, component reflectance, optical splitters, accumulated loss, dual wavelength testing, bi-directional testing, and pass/fail analysis.."],
    # 49
    ["A. At the output of a forward amplifier because the forward levels are highest and the return levels are lowest.",
     "B.Three separate types of activities: identification, location, and resolution.",
     "C.First, the technician at the receiver location (headend) should measure and document the optical input power level (measured in dBm) using a power meter.",
     # 50
     "D.That there are high micro-reflections and that the cause is near the modem, likely in the drop system."],
]
#OPTIONS------------------------------------------------------------------OPTIONS#
d3_correct_answers = ["C", "D", "C", "A", "A", "D", "C", "C", "B", "B", "D", "B", "A", "B", "B", "B", "A", "C", "D",
                      "A", "C", "D", "B", "C", "D", "A", "A", "A", "C", "C", "D", "B", "A", "A", "D", "B", "C", "A",
                      "D", "B", "B", "A", "B", "C", "A", "C", "D", "B", "D", "C", "A", "C", "D", "B", "D", "C", ]

# List of correct answers for d3 test
# ----------------------------------------------------------------#
installer_technician_conventional = ["A.",
                         "B.",
                         "C.",
                         "D."],  # List of options for fiber
#------------------------------------------------------------------#
installer_technician_conventional_questions = ["How old are you?"]
#------------------------------------------------------------------#
installer_technician_conventional_answers = ["a"]
#------------------------------------------------------------------#

###############email generator#####################
class EmailGenerator:
    def __init__(self):
        # emails below
        self.emails = {
            "3000452": "example@gmail.com",
            "353": "example1@gmail.com",
            # emails above
        }

    def get_email(self, number):
        number_str = str(number)

        # Retrieve the email address based on the number
        return self.emails.get(number_str, "No email found for this number.")


###################  region generator  ##################

class StateInfo:
    def __init__(self):
        self.state_info = {
          #Highsplit

          "standard":"HS_STANDARD- used for all new taps, and existing taps that are still working at standard drop levels and within 150’ from the tap. Standard drops will require the tap to be within optimal signal ranges.",


          "hot":"HS_HOT- used for existing long drop scenarios where more signal is needed on the drop route to reach a customer that is further (150’-250’) from the tap than the standard drop accounts for. Hot drop will add 3dB to the minimum forward levels and decrease return levels at the tap by 3dB.",


          "fudge":"HS_FUDGE- used when existing taps are failing with Standard or Hot drops, but not outside of the window of signal ranges that should work and would eliminate the need to change a tap that is failing at other levels. See more below on when to apply the HS_FUDGE drop.",


          "wifi":"HS_WIFI- used when the tap is being placed to feed a Wi-Fi access point (AP) in a HS design. WiFi drops require much less signal than a standard drop due to the short distance between the tap and the Wi-Fi AP, and the input levels of the Wi-Fi AP being so low.",
          #end of highsplit
                    "alabama cables" : """Primary Trunk Cable: 875P3 all new construction 
750P3 older existing plant
Primary Feeder Cable: 625P3 all new construction 
500P3 older existing plant""",
            "alabama coax equipment" :
""" Coax Equipment Standards
[Cascade Limit: All 870 MHz design areas are N+6. All 1 GHz design is N+2 max.]

[Tap Manufacturers:SA1G
Available Tap Values:  You do not have to remove taps but above 26 but you can not place them. 4-24 are the available taps. 4 port is the minimum allowed ports for this area
Coupler Manufacturer: SA
Coupler Models: DC16, DC12, DC08, 2WAY
Multi Split Manufacturer: SA
Multi Split Models: 3WAY]

[ASSIVES:Active Models: C-Cor Birmingham/Cisco (South and FL)
C-COR - 1GHZAMPS: 1GHZ7BA, 1GHZ7TBA, 1GHZ7LEA
Cisco (SA) – 1GHZSA: 1GSA7LEA, 1GSA7LEM, 1GSA7HGBT]""",
            "alabama power supply info":"""Power Supply Model: AL_XM3_18_90_2_SB
Power Supply Max Load: 80% or 14.4a out of 18""",
            "alabama naming standards":
"""
[The power supply takes on the node boundary names that it is located. The first supply will be the A supply.]

S[TATUS MONITORING: Status monitoring, a tap will locate within 200’ of the supply. New design will place a tap at the PS location, or run signal back on the power jumper and place the inserter at the PS.]

[NODE NAMING: All nodes are 7 digit node numbers. The first 2 characters are the hub number, the next 2 places are for HHD or virtual hub info, and the last 3 numbers are sequential.]

[ACTIVE NAMING: Active names 10 characters – 7 are the node name. The 8th position is the power supply letter and the last 2 digits is an arbitrary number.]""",
            "alabama wifi designs":
"""1. Wi-Fi designs are placed as an amplifier requiring a max input of 10db off a DC.
2. Wi-Fi names follow the amplifier naming convention – adding a W at the end.
a) Example: Wi-Fi 210000B23W
3. All placed using Cisco WiFi AP1552C""",
          #california-begins here-
          "bakersfield coax cables": #Bakersfield, California
                    """Cables:
          PRIMARY TRUNK CABLE:
          BHN 750P3 / 750P3UG
          SUDDEN LINK .750JC / AER .750JCF / UG .875JC / AER .875JCF / UG

          Primary Feeder Cable:
          BHN .412P1 /.412P1UG /.500P3 .500P3UG
          SUDDEN LINK .500JC / AER .500JCF / UG .625JC / AER .625JCF / UG
                    """,
                    "bakersfield coax equipment":
          """Passives:
          TAPS: 
          BHN (2v4 – 26) (4v8 – 26) (8v12 – 26)
          SUDDEN LINK (2v4 – 26) (4v8 – 26) (8v 12 – 26)

          Coupler Manufacturer: BHN LINDSAY / SUDDEN LINK GI
          Coupler Models: BHN 2 WAY DC-8 DC-12 / SUDDEN LINK 3K 7K 9K 12K

          Multi Split Manufacturer: BHN LINDSAY / SUDDEN LINK GI
          Multi Split Models: BHN LLS103 / SUDDEN LINK 3636K

          Notes:
          26 VALUED TAPS ARE NOT BEING USED ANY MORE DUE TO RETURN / CHANGING EXISTING 26 TAPS WHEN POSSIBLE TO 23 VALUED


          Active Models:
          BHN AMPS ( TYPE1 TRUNK OUT 39/27 FEEDER OUT 47/35 ) ( TYPE2 FEEDER 47/35 )
          BHN LINE EXTENDERS ( 1st CASCADE TYPE3T 47/35 THERM ) ( 2nd CASCADE TYPE3A 44/32 AGC ) ( 3rd CASCADE TYPE3T3 42/30 THERM ) SEE NOTES BELOW
          -
          SUDDEN LINK AMPS ( BTD0000A 44/34 )
          SUDDEN LINK LINE EXTENDERS ( BTD00000 44/34 )

          Notes:
          BHN CHANGING: OUTPUTS ON AMPS TO (TRUNK OUT 40/30 FEEDER 46/36) ALSO CHANGING THE DE-RATING OF LINE EXTENDERS TO ALL FLAT (46/36)
          SUDDEN LINK: CHANGING ALL TRUNK AMPS & LINE EXTENDERS TO (46/36)

          Cascade Limit:
          BHN: 6 IN CASCADE NO EXEMPTIONS ( 3 AMPS 3 LINE EXTENDERS ) 
          NEW DESIGN: N+1 WILL BREAK RULE IN COMMERCIAL AREAS
          SUDDEN LINK: NO CASCADE LIMITS
          """,
                    "bakersfield power info":
          """"Power Supply Info:
          Power Supply Model:
          BHN STNDBY 15A & STNDBY 18A
          SUDDEN LINK STNDBY 15A & STNDBY 18A
          Power Supply Max Load:
          BHN POWER SUPPLY MODEL: STNDBY 80% AT 15A & STNDBY 80% AT 18A
          SUDDEN LINK POWER SUPPLY MODEL: 15A MAX LOAD 14A & 18A MAX LOAD 16.7A

          BHN & SUDDEN LINK BOTH DO STATUS MONITORING
          """,
                    "bakersfield naming standards": 
          """ 
          Node Naming
          EXAMPLE-A222
          A = HUB 222 = NODE NUMBER

          Active Naming:
          EXAMPLE-A222302C
          A = HUB 222 = NODE NUMBER 3 = POWER SUPPLY NUMBER 02 = AMP NUMBER C = LE LETTER

          Power Supply Naming Standards: 
          EXAMPLE:-A2223
          A = HUB 222 = NODE NUMBER 3 = POWER SUPPLY NUMBER
          """,
                    "bakersfield wifi designs":"See Image",
          #Florida-begins here-
          #East Florida 
                     "east florida cables" : """
          Primary Trunk Cable:
          A875NEW (Aerial applications) & B875NEW (Underground & power jumper applications) when designing new.
          Primary Feeder Cable: 
          A625NEW (Aerial applications) & B625NEW (Underground & power jumper applications) when designing new.
          Notes:
          Cable inside buildings will be designed with cables called out by field engineer.
          A875NEW, B875NEW, A625NEW & B625NEW cables will be changed to A875, B875, A625 & B625 at time of asbuilt.""",
                     "east florida coax equipment" :
          """ Taps:
          GI / Jerrold/ Motorola

          Splitters & power inserters:
          GI / Jerrold / Motorola
          Note: 
          1. Tap Manufacturer: Arris series taps should be used for all new designs
          2. No 23V taps or DC + tap combination exceeding 23V
          3. Amplifiers – Cisco 1GHz Gainmaker high gain singles, dual and balanced triples are used in new design. AGC amplifiers are used. No thermals are used in design.
          """, 
                       "east florida power supply info":
          """east florida power supply info: 
          Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18

          Status Monitoring:
          Status Monitoring feed is designed at the power supply location. DC16’s / new dedicated tap or increasing an available tap port by 1 is required for the feed.
          Note: 
          Max feed levels 15dB. Min feed levels 3dB.
          Coax note indicating type of port dedicated for status Monitoring place at the location.
          """,
                       "east florida naming standards":
          """Nodes: 
          Nodes names ending in numeric - Node name + alpha digit beginning with A - example 3 power supplies in node BA011 – power supply names will be BA011A, BA011B, BA011C.


          Nodes names ending in alpha - Node name + numeric digit beginning with 1 - example 3 power supplies in node CAZ – power supply names will be CAZ1, CAZ2, CAZ3. Note CAZ1 should be the power supply powering the node.

          Active naming: 
          Amp numbering is as follows - Number + Amp Type Number + Location (A – aerial U – underground)
          Example 38-12A
          """,
                      "east florida wifi designs":
          """
          1. Wifi design feeds are DC’s. No power passing taps are used.
          2. Max input to a Cisco CA1552C WIFI AP is 10dB
          3. Max input to a Bellaire / Ericson BA100SN WIFI AP is 15dB
          4. Wifi ap names are node name +W(indicating wifi) + # example BD101W01
          5. Wifi meshed ap names are egress ap number+M(mesh unit)+number . example BD011W01M01
          6. No more than 5 ap’s in a mesh cluster which includes the egress ap. One egress ap per cluster.
          7. For Public (SSID Cable Wifi transmitted)Wifi ap name and project name are added and saved to userfield1 (AP name)and userfield2 (Project name) during a device single review for ICOM’s notification / BHN wifi hotspot location map .
          8. For Private MDU / Enterprise Wifi ap name and the text”MDU “are added and saved to userfield1 (AP name) and userfield2 (MDU) during a device single review for ICOM’s notification.
          9. Bentley V8i Wifi AP devices are selected from the tap’s menu. Series name is WIMxAP. Two types are used Bellaire / Ericson BA100SN (Bentley cell – WTF) and Cisco CA1552C (Bentley cell – WTF2).
          """,
                      #north florida
          "north florida cables" : """Primary Trunk Cable: 875P3 all new construction 
750P3 older existing plant
Primary Feeder Cable: 625P3 all new construction 
500P3 older existing plant""",
            "north florida coax Equipment" :
""" Coax Equipment Standards
[Cascade Limit: All 870 MHz design areas are N+6. All 1 GHz design is N+2 max.]

[Tap Manufacturers:SA1G
Available Tap Values:  You do not have to remove taps but above 26 but you can not place them. 4-24 are the available taps. 4 port is the minimum allowed ports for this area
Coupler Manufacturer: SA
Coupler Models: DC16, DC12, DC08, 2WAY
Multi Split Manufacturer: SA
Multi Split Models: 3WAY]

[ASSIVES:Active Models: C-Cor Birmingham/Cisco (South and FL)
C-COR - 1GHZAMPS: 1GHZ7BA, 1GHZ7TBA, 1GHZ7LEA
Cisco (SA) – 1GHZSA: 1GSA7LEA, 1GSA7LEM, 1GSA7HGBT]""",
            "north florida coax equipment" :
"""North Florida Power supplyPower Supply:
[The power supply takes on the node boundary names that it is located. The first supply will be the A supply.]

S[TATUS MONITORING: Status monitoring, a tap will locate within 200’ of the supply. New design will place a tap at the PS location, or run signal back on the power jumper and place the inserter at the PS.]

[NODE NAMING: All nodes are 7 digit node numbers. The first 2 characters are the hub number, the next 2 places are for HHD or virtual hub info, and the last 3 numbers are sequential.]

[ACTIVE NAMING: Active names 10 characters – 7 are the node name. The 8th position is the power supply letter and the last 2 digits is an arbitrary number.]""",
            "north florida wifi designs":
"""1. Wi-Fi designs are placed as an amplifier requiring a max input of 10db off a DC.
2. Wi-Fi names follow the amplifier naming convention – adding a W at the end.
a) Example: Wi-Fi 210000B23W
3. All placed using Cisco WiFi AP1552C""",
          #Green Bay
          "green bay cables":
          """Cables:
Primary Trunk Cable: 875P3
Primary Feeder Cable: 625P3
          """,
          "green bay coax equipment":
"""Passives:
Tap Manufacturer: Antronix
Available Tap Values: 4-23/24
Coupler Manufacturer: SA
Coupler Models: SAS2MM, SADC8MM
Multi Split Manufacturer: SA
Multi Split Models: SAS3UMM
Notes: DC12s are not to be used in design. Splits are delineated between feeder and trunk

Actives:
Amplifiers: GNMR HGD TRUNK, GNMR UBT
Line Extenders: GNMR LE A, GNMR LE T, GNMR HGD LE

Cascade:
Internal Splits cannot be placed in Type 1s
No more than 3 LE’s can be used in cascade
No More than 2 of these actives can be placed in a row: TYPE2LE, TYPE2LE1, GNMR HGD LE""",
          "green bay power info":
""""Power Supply Info:
Power Supply Model: AL_XM3_18_90_2_SB
Power Supply Max Load: 80% or 14.4a out of 18
Status Monitoring:

All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.
The tap will be designed like a normal tap and should never be placed in trunk. If there is an existing tap within standard drop distance from the PS with an open port, then a port from that tap can be used as a Status Monitor. All Status Monitoring should be documented in V8i with a STATM cell by the PS with a COAXMISCLINE pointing to the tap. If necessary, a tap can be cut in on an adjacent node as long as the tap remains within standard drop distance from the new PS
""",
          "green bay naming standards": 
""" 
Node naming standards: 
Node Name +  Alpha Letter

Active naming standards:
Node Name | Active # | Feeder α
""",
          "green bay wifi designs":"none for this area",
           #Georgia
          "georgia cables" :
"""Primary Trunk Cable: 
Primary trunk cable for all systems is .875Aer, .875U
Primary Feeder Cable: 
Primary feeder cable for all systems is .625Aer, .625U""",
            "georgia coax equipment":
"""[The tap information is not yet defined. Your nearest tap is your friend]
[Some of the 750 and 550 systems have areas where the cascade is greater than 6.
No new designs can be greater than the highest existing cascade within that node. The only exception is where nodes that were originally planned as N+4.

Notes: Trunk amps are AGC
note: 11 value or less taps will need to have an EQ with a return conditioner or a bypass EQ with a return conditioner
note: NO actives directly off the down leg of a dc without manager approval.]

[Cascade Limit: All 870 MHz design areas are N+6. All 1 GHz design is N+2 max.
Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check]""",
            "south carolina power supply":
"""Power Supply Model: Alpha XM3 90V 18A
Power Supply Max Load: 90% or 16.2a out of 18""",
          
            "georgia naming standards":
"""status monitoring: RF-SPI equipment is used for status monitoring in all areas of the Carolinas. The inserter must be placed and terminated off the high loss leg of a DC-12, Use RF-SPI inserter symbol if available in that spec file.
POWER SUPPLY NAMING:
[Power Supply:Power supplies are identified with a single alpha character]

[STATUS MONITORING: 
Status monitoring, a tap will locate within 200’ of the supply. New design will place a tap at the PS location, or run signal back on the power jumper and place the inserter at the PS.]

[NODE NAMING: 
i.e. AH118001
AH1180 01
Node name Active#
Node will always be active # 01. Charter will supply all new node names.]

[ACTIVE NAMING: 
i.e AH118017
AH1180 01
Node name Active#
The first six characters stay the same for every active.
The active # is a random number starting with one and increasing with each active off the node.]""",
            "georgia wifi designs":"This document is not yet defined",
          #Indiana Begins here
          #Is midwest columbus...indiana?? I guess
                     "midwest columbus cables" : 
          """
          Primary Trunk Cable:
          860QR
          Primary Feeder Cable: 
          540QR

          Note: Trunk cable has been approved for use in feeder only when max cascade was met or PS load was met and significant cost savings were to be had!!!
          """,
                     "midwest columbus coax equipment" :
          """Tap Manufacturer:
          Varies
          4-23/24
          Coupler Manufacturer:
          ARRIS 9TFC
          Coupler Models: 
          9TFC12 / 9TFC8 / 9TFC4 / 9TF12D / 9TFC8D / 9TFC4D
          Multi Split Manufacturer: ARRIS 9TFC
          Multi Split Models: 488T/488D

          note(for tap models): 
          Antronix Taps[ In Alphabetical order]:
          1. Bluffton 38N211-216, Bowling Green 36N301-329 & 36N331407, Delphos, Findlay,Fostoria, Fremont,Gibsonburg, Green Springs, Lima,Moulton, North Baltimore 36N501511/36N135/36N330 ,Ottawa, Rockford, Sycamore, Walbridge, Waynesfield.
          !When  designing these hubs; legacy ARRIS TAPS, will be swapped with Antronix TAPS!
          2. Change all none PRE-EXISTING taps from 8/2 -> 8/4.

          note (for actives): 
          1. GS7000 are for all new nodes 
          2. 901s are for all new amps
          3. 331_AGC are for all new LINE extenders Actives 
          4. 1G CCOR Internals arent allowed 
          5. Mini's will use plug in actives.""", 
                       "midwest columbus power supply info":
          """Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18
          Notes: PI in feeder only; if only feeder exists, then the CC needs to make the call on placement.
          Status monitoring: All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must designed at all new supply locations.
          The tap will be designed like a normal tap and should never be placed in trunk. If there is an existing tap within standard drop distance from the PS with an open port, then a port from that tap can be used as a Status Monitor. All Status Monitoring should be documented in V8i with a STATM cell by the PS with a COAXMISCLINE pointing to the tap. If necessary, a tap can be cut in on an adjacent node as long as the tap remains within standard drop distance from the new PS""",
                       "midwest columbus naming standards":
          """Node naming:
          Hub + Node + Leg(#) + cascade
          i.e. 12-1200-00

          Power: 
          Node Name Alpha Letter Hub Name
          i.e. 004A13

          Active naming: 
          Hub + Node + Leg(#) + Cascade from node(#) + cascade from split(#) + split (#) + feeder (Letter)
          i.e. 12-1212-11A""",
                      "midwest columbus designs":"None for this area",
          #kentucky
            "kentucky cables":
"""Primary Trunk Cable: .860QR. Terre Haute, IN: 875P3
Primary Feeder Cable: .540QR. Terre Haute, IN: 625 P3
Powering cable: 540QR
With such differentiating standards andancient forms of communication, this could very well be off depending on your city. But is mostly right.""",
            "kentucky coax equipment":
"""Coax equipment standards
[2/4 is the only two port allowed. Other than that
With such differentiating standards, the most efficient way to know which tap to use is to click the one next to you. Often, autodraft will do it right. ]

CASCADE
[Cascade Limit: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
That said – if you’re adding greater than a commercial/tni order]
The rest of the information is not yet defined""",
            "kentucky Power Info":
"""AL_XM3_18_90_2_SB
max load 14.4""",
            "kentucky naming standards":
"""POWER SUPPLY NAMING
Power Supply:[Node Name][Letter]

STATUS MONITORING:
For all Node Splits and new power supplies a TAP must exist or be added at the Power Supply for Status Monitoring.
If a tap is already present & has an open port – it can be used for status monitoring. If all ports are full or there is no tap at that location – then you must add one.

NODE NAMING: 
With such differentiating standards. It is best to search your area

ACTIVE NAMING: 
With such differentiating standards. It is best to search your area""",
            "kentucky wifi designs":"This document is not yet defined",
          #Milwaukee
          "milwaukee cables":
 """Cables:
Primary Trunk Cable: 875SF (OSP) 875P3 (ISP)
Primary Feeder Cable: 625SF (OSP) & 625P3 (ISP)""",
          "milwaukee coax equipment":
"""Passives:
Tap Manufacturer: Antronix (new), Maspro (existing)
Available Tap Values: 4-23/24
Coupler Manufacturer: Varies
Coupler Models: LDC102/LDC108
Multi Split Manufacturer: Varies
Multi Split Models: LLS103
Notes: DC12s are not to be used in design. Splits are delineated between feeder and trunk. Taps are not to be rotated except on actives & EOLs

Cascade:
Up to 2 Amps can be placed in line
Up to 4 Les can be placed in line, must be derated
 """,
          "milwaekee power supply info":
"""Power Supply Info:
Power Supply Model: AL_XM3_18_90_2_SB
Power Supply Max Load: 80% or 14.4a out of 18
          """,
          "milwaekee naming standards":
"""Node:
Franchise Code +  Node Name
Active:
Node Name Supply ID Active # Franchise Code
note: On Active Naming, the first 5 characters stay the same for every active (except on seg nodes)
Power supply:
Node Name + Alpha Letter
""",
          "milwaukee wifi designs":"No wifi designs for this area",
          
          #North Carolina
            "north carolina cables" :
"""Primary Trunk Cable: Primary trunk cable for all systems is .875Aer, .875U
Primary Feeder Cable: Primary feeder cable for all systems is .625Aer, .625U""",
            "north carolina coax equipment":
"""[The tap information is not yet defined. Your nearest tap is your friend]
[Some of the 750 and 550 systems have areas where the cascade is greater than 6.
No new designs can be greater than the highest existing cascade within that node. The only exception is where nodes that were originally planned as N+4.

Notes: Trunk amps are AGC
note: 11 value or less taps will need to have an EQ with a return conditioner or a bypass EQ with a return conditioner
note: NO actives directly off the down leg of a dc without manager approval.]

[Cascade Limit: All 870 MHz design areas are N+6. All 1 GHz design is N+2 max.
Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check]""",
            "north carolina power supply info":
"""Power Supply Model: Alpha XM3 90V 18A
Power Supply Max Load: 90% or 16.2a out of 18""",
            "north carolina naming standards":
"""status monitoring: RF-SPI equipment is used for status monitoring in all areas of the Carolinas. The inserter must be placed and terminated off the high loss leg of a DC-12, Use RF-SPI inserter symbol if available in that spec file.
POWER SUPPLY NAMING:
[Power Supply:Power supplies are identified with a single alpha character]

[STATUS MONITORING: 
Status monitoring, a tap will locate within 200’ of the supply. New design will place a tap at the PS location, or run signal back on the power jumper and place the inserter at the PS.]

[NODE NAMING: 
i.e. AH118001
AH1180 01
Node name Active#
Node will always be active # 01. Charter will supply all new node names.]

[ACTIVE NAMING: 
i.e AH118017
AH1180 01
Node name Active#
The first six characters stay the same for every active.
The active # is a random number starting with one and increasing with each active off the node.]""",
            "north carolina wifi designs":"This document is not yet defined",
           #South Carolina
            "south carolina cables" :
"""Primary Trunk Cable: Primary trunk cable for all systems is .875Aer, .875U
Primary Feeder Cable: Primary feeder cable for all systems is .625Aer, .625U""",
            "south carolina coax equipment":
"""[The tap information is not yet defined. Your nearest tap is your friend]
[Some of the 750 and 550 systems have areas where the cascade is greater than 6.
No new designs can be greater than the highest existing cascade within that node. The only exception is where nodes that were originally planned as N+4.

Notes: Trunk amps are AGC
note: 11 value or less taps will need to have an EQ with a return conditioner or a bypass EQ with a return conditioner
note: NO actives directly off the down leg of a dc without manager approval.]

[Cascade Limit: All 870 MHz design areas are N+6. All 1 GHz design is N+2 max.
Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check]""",
            "south carolina naming standards":
"""status monitoring: RF-SPI equipment is used for status monitoring in all areas of the Carolinas. The inserter must be placed and terminated off the high loss leg of a DC-12, Use RF-SPI inserter symbol if available in that spec file.
POWER SUPPLY NAMING:
[Power Supply:Power supplies are identified with a single alpha character]

[STATUS MONITORING: 
Status monitoring, a tap will locate within 200’ of the supply. New design will place a tap at the PS location, or run signal back on the power jumper and place the inserter at the PS.]

[NODE NAMING: 
i.e. AH118001
AH1180 01
Node name Active#
Node will always be active # 01. Charter will supply all new node names.]

[ACTIVE NAMING: 
i.e AH118017
AH1180 01
Node name Active#
The first six characters stay the same for every active.
The active # is a random number starting with one and increasing with each active off the node.]""",
            "south carolina wifi designs":"This document is not yet defined",
          #eastern north carolina
            "eastern north carolina coax equipment":
"""Primary Trunk Cable:
Primary Trunk cable for all systems is 875P3
Primary Feeder cable: 
Primary Feeder cable is 625P3

Passives:
Tap Manufacturer: MGT2200, MGT2400, and MGT2800
Available Tap Values: 4-23
Coupler Manufacturer: ANTRONIX
Coupler Models: 2Way = SGHz2 DC8 = MGDC2108 DC12 = MGDC2112
Multi Split Manufacturer: Varies
Multi Split Models: SGHz3A
Notes: 2Port23 Taps will be placed as 4Port23 even if the House Count is 2 or under. 26/29 Value taps will not be placed down during new design

Actives:
Active Models: Models will vary per spec file
On new Designs, 1GIG_NEW will be used for all areas
1GIG_New, 1GIG_CST, T_1GIG_NEW, WLM_DI1G & 870_NEW:

Nodes: OM4100
Amplifiers: FMB901 (Dual)
Line Extenders: FM331TLC (Thermal) & FM331ALC (AGC)

DURCH750:
Nodes: OM4100
Amplifiers: FMB901
Line Extenders: FM331TLC & FM331ALC

JACK750:
Nodes: OMAX4100
Amplifiers: FMB901E
Line Extenders: LETFM331 & LEAFM331

NEWP750 & WILMA750:
Nodes: OMAX4100
Amplifiers: FMB901E
Line Extenders: LETFM331 & LEAFM331

Colum862:
Nodes: OM4100
Amplifiers: FMTB901E (Dual) & FMB901Ele (Feeder Dual)
Line Extenders: FM331A (AGC) & FM331T (Thermal)

Note: Raleigh, Wilmington and Fayetteville: Moving an existing LE means changing it to AGC
Wilmington, Jacksonville, Newport Swansboro: All new nodes are OM4100S(c-cor)
            """,
          "eastern north carolina naming standards":
""""eastern north carolina power supply info:
Power Supply Model: AL_XM3_18_90_2_SB
Power Supply Max Load: 90% or 16.2a out of 18
""",
          "eastern north carolina naming standards":
"""Node Naming:
Hub | Node # | Power Supply α | Trunk Active # |
Active Naming:
Hub | Node # | Power Supply α | Trunk Active # | Feeder Active α |
 
Status Monitoring:
All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, RF-SPI equipment is used for status monitoring in all areas of the Carolinas. The inserter must be placed and terminated off the high loss leg of a DC-12, Use RF-SPI inserter symbol if available in that spec file.
""",
          "eastern north carolina wifi designs":
"""WiFi How to:
Forward Levels (550MHz-750MHz): 45dB (±10dB)
Return Levels (5MHz-42MHz): 0dB (±6dB)

All Wifi designs consist of an Access Point (AP) and a Wifi device. An AP is a power passing tap that is cut into the existing plant whereas the Wifi device is an active that is connected to the port of the tap.
""",
           
          #Tennesee(AL)
            "tennesee cables":#Tennesee(AL)
"""cables 
Primary Trunk Cable: 875 P3
Primary Feeder Cable: 625 P3
Powering Cable: 625 Power Fdr""",
            "tennesee coax equipment":
"""[Tap Manufacturer: 
NA
Available Tap Values: 
4-24
Coupler Manufacturer: 
SA
Coupler Models: 
SAS2MM-15A, SADC8MM-15A, SADC12MM-15A
Multi Split Manufacturer: 
SA
Multi Split Models:
SAS3UMM-15A
Notes: 
Do not use taps over 24 value.
Active Models:
Trunk – GNMKR HGD(if approved)
Line Extenders – GMKR1G LE]

[Cascade Limit: All 870 MHz design areas are N+6. All 1 GHz design is N+2 max.
Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check]""",
            "tennesee power supply info":
"""Power Supply Model:
Alpha XM3 90V 18A
Power Supply Max Load: 
80% or 14.4a out of 18.""",
          
            "tennesee naming standards":
"""STATUS MONITORING:
Place tap at supply for status monitoring or use existing tap port
May be attached to leg of split also
Must be drafted at 0° rotation.

NODE NAMING:
HE/Hub code + ###
e.g., AB001
Node will always be active # 01. Charter will supply all new node names.
Segmented Nodes:
HE/Hub code + ###+Port
e.g., AB001A

POWER SUPPLY NAMINGz;
Power Supply:Single alpha Character e.g., A, B, C etc

ACTIVE NAMING: 
Single alpha Character e.g., A, B, C etc""",
            "tennesee wifi designs":"This document is not yet defined",
          #Louisiana (AL)
                        "louisiana cables":#Louisiana (AL)
"""cables 
Primary Trunk Cable: 875 P3
Primary Feeder Cable: 625 P3
Powering Cable: 625 Power Fdr""",
          
            "louisiana coax equipment":
"""[Tap Manufacturer: 
NA
Available Tap Values: 
4-24
Coupler Manufacturer: 
SA
Coupler Models: 
SAS2MM-15A, SADC8MM-15A, SADC12MM-15A
Multi Split Manufacturer: 
SA
Multi Split Models:
SAS3UMM-15A
Notes: 
Do not use taps over 24 value.
Active Models:
Trunk – GNMKR HGD(if approved)
Line Extenders – GMKR1G LE]

[Cascade Limit: All 870 MHz design areas are N+6. All 1 GHz design is N+2 max.
Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check]""",
            "louisiana power supply info":
"""Power Supply Model:
Alpha XM3 90V 18A
Power Supply Max Load: 
80% or 14.4a out of 18.""",
            "louisiana naming standards":
"""STATUS MONITORING:
Place tap at supply for status monitoring or use existing tap port
May be attached to leg of split also
Must be drafted at 0° rotation.

NODE NAMING:
HE/Hub code + ###
e.g., AB001
Node will always be active # 01. Charter will supply all new node names.
Segmented Nodes:
HE/Hub code + ###+Port
e.g., AB001A

POWER SUPPLY NAMINGz;
Power Supply:Single alpha Character e.g., A, B, C etc

ACTIVE NAMING: 
Single alpha Character e.g., A, B, C etc """,   
          #Texas (texas regions begin here)
          #tex-mex
          "tex-mex":"""TEX-MEX IS SEPERATED BY THEIR 'REGIONS', TRY THE SAME COMMAND BUT ENTER BORDER CORRIDOR, CORPUS CHRISTI, RIO GRANDE, LAREDO, OR ROCKPORT + what youre looking for.""",
          "texmex":
          """TEX-MEX IS SEPERATED BY THEIR 'REGIONS', TRY THE SAME COMMAND BUT ENTER BORDER CORRIDOR,
          CORPUS CHRISTI, RIO GRANDE, LAREDO, OR ROCKPORT + what youre looking for.""",
          #BORDER CORRIDOR
          "border corridor coax cables": #BORDER CORRIDOR
                    """Cables:
          Primary Trunk Cable: 875P3
          Primary Feeder Cable: 625P3
                    """,
                    "green bay coax equipment":
          """Passives:
          TAPS: 
          Antronix: 
          4-23

          Multisplit models: 
          Antronix

          COUPLERS:
          MGLS3

          SPECFILE:
          BC1002

          TRUNK:
          1GHz UBT 
          1GHz TRUNK

          LE:
          1GHz HGD LE
          1GHz LE

          1. Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
          That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check
          2. MTU's and Subdivisions will limit the cascading of amplifiers for an HFC Architecture plant to Node +2 (N2)..
          """,
                    "border corridor power info":
          """"Power Supply Info:
          Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: AL_XM3_18_90_2_SB 
          80% or 14.4a out of 18
          Status Monitoring:

          Placed as a cell on the Power Supply.
          All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.
          In Laredo, install a DC16 at each standby power supply location for the insertion of the signal from a status monitoring unit.
          """,
                    "border corridor naming standards": 
          """ 
          Node naming standards: 
          Node Name +  sequential number

          Active naming standards:
          HUB + NODE + POWER SUPPLY + AMP NUMBER
          """,
                    "border corridor wifi designs":"none for this area",
           #CORPUS CHRISTI
          "corpus christi coax cables": 
                    """Cables:
          Primary Trunk Cable: 875P3
          Primary Feeder Cable: 625P3
                    """,
                    "corpus christi coax equipment":
          """Passives:
          TAPS: 
          Antronix: 
          4-23

          Multisplit models: 
          MGLSH3
          MGLSH3B

          SPECFILE:
          BC1002

          COUPLERS: 
          MGLS2
          MGDC2108
          MGDC2112

          TRUNK:
          FM901e TRNK

          LE:
          FM331 LE ALC

          1. Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
          That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check
          2. MTU's and Subdivisions will limit the cascading of amplifiers for an HFC Architecture plant to Node +2 (N2)..
          """,
                    "border corridor power info":
          """"Power Supply Info:
          Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: AL_XM3_18_90_2_SB 
          80% or 14.4a out of 18
          Status Monitoring:

          Placed as a cell on the Power Supply.
          All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.
          In Laredo, install a DC16 at each standby power supply location for the insertion of the signal from a status monitoring unit.
          """,
                    "corpus christi naming standards": 
          """ 
          Node naming standards: 
          Node Name +  sequential number

          Active naming standards:
          [Hub name + sequential number + PS letter + Amp number + “00”]
          (Amp number of node is always 1. 00 is used as place holder)
          """,
                    "corpus christi wifi designs":"none for this area",
          #ROCKPORT
          "rockport coax cables": 
                    """Cables:
          Primary Trunk Cable: 875P3
          Primary Feeder Cable: 625P3
                    """,
                    "rockport coax equipment":
          """Passives:
          TAPS: 
          Antronix: 
          4-23

          Multisplit models: 
          MGLSH3
          MGLSH3B

          SPECFILE:
          RP1GZ

          COUPLERS: 
          MGLS2
          MGDC2108
          MGDC2112

          TRUNK:
          FM901e TRNK

          LE:
          FM331 LE ALC

          1. Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
          That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check
          2. MTU's and Subdivisions will limit the cascading of amplifiers for an HFC Architecture plant to Node +2 (N2)..
          """,
                    "rockport power info":
          """"Power Supply Info:
          Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: AL_XM3_18_90_2_SB 
          80% or 14.4a out of 18
          Status Monitoring:

          Placed as a cell on the Power Supply.
          All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.
          In Laredo, install a DC16 at each standby power supply location for the insertion of the signal from a status monitoring unit.
          """,
                    "rockport naming standards": 
          """ 
          Node naming standards: 
          Node Name +  sequential number

          [Hub name + sequential number + PS letter + Amp number + “00”]
          (Amp number of node is always 1. 00 is used as place holder)
          """,
                    "rockport bay wifi designs":"none for this area",
          #LAREDO
          "laredo coax cables": 
                    """Cables:
          Primary Trunk Cable: 875P3
          Primary Feeder Cable: 625P3
                    """,
                    "laredo coax equipment":
          """Passives:
          LAREDO 1G TAPS: 
          4-23/REGAL
          LAREDO 750/860 TAPS:
          4-32/ANTRONIX


          Multisplit models: 
          LAREDO 1G: 
          REGAL - RLS10-3
          LAREDO 750/860 TAPS:
          LINDSAY - LLS103

          SPECFILE:
          LAREDO 1G: 
          FMT901e
          LAREDO 750:
          FNT700 E71CJ E70CJ
          LAREDO 860:
          FMT901e TB FMB901e TMB

          COUPLERS: 
          LAREDO 1G: 
          REGAL
          LAREDO 750/860:
          LINDSAY

          TRUNK:
          LAREDO 1G: 
          FMT901e
          LAREDO 750:
          FNT700
          E71CJ 
          E70CJ
          LAREDO 860:
          FMT901e TB
          FMB901e TMB

          LE:
          LAREDO 1G : 
          FML331T 
          FML331A 
          FMB LE
          LAREDO 750:
          E72CJ-T 
          E72CJ-A 
          FNT700 
          FNB LE
          LAREDO 860:
          FM331
          FMT901e LE 
          FMB901e

          1. Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
          That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check
          2. MTU's and Subdivisions will limit the cascading of amplifiers for an HFC Architecture plant to Node +2 (N2)..
          """,
                    "laredo supply power info":
          """"Power Supply Info:
          Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: AL_XM3_18_90_2_SB 
          80% or 14.4a out of 18
          Status Monitoring:

          Placed as a cell on the Power Supply.
          All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.
          In Laredo, install a DC16 at each standby power supply location for the insertion of the signal from a status monitoring unit.
          """,
                    "laredo naming standards": 
          """ 
          Node naming standards: 
          Node Name +  sequential number

          Active naming standards:
          HUB + NODE + POWER SUPPY + AMP # + LE SEQUENCE(A)
          """,
                    "laredo wifi designs":"none for this area",
          #RIO GRANDE
          "rio grande coax cables": 
                    """Cables:
          Primary Trunk Cable: 875P3
          Primary Feeder Cable: 625P3
                    """,
                    "rio grande coax equipment":
          """Passives:
          TAPS: 
          Antronix
          4-23

          Multisplit models: 
          MGLSH3

          SPECFILE:
          RGV870

          COUPLERS: 
          ANTRONIX
          MGLS2
          MGDC2108 
          MGDC2112

          TRUNK:
          870 UBT 
          870 TRUNK

          LE:
          870 LE 870 HGD LE

          1. Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
          That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check
          2. MTU's and Subdivisions will limit the cascading of amplifiers for an HFC Architecture plant to Node +2 (N2)..
          """,
                    "rio grande power info":
          """"power supply info:
          Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: AL_XM3_18_90_2_SB 
          80% or 14.4a out of 18
          Status Monitoring:

          Placed as a cell on the Power Supply.
          All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.
          In Laredo, install a DC16 at each standby power supply location for the insertion of the signal from a status monitoring unit.
          """,
                    "rio grande naming standards": 
          """ 
          Node naming standards: 
          Node Name +  sequential number

          Active naming standards:
          HUB + NODE + POWER SUPPLY + ACTIVE SEQUENCE (01)
          """,
                    "rio grande wifi designs":"none for this area",
          "north texas dallas cables":
"""Primary Trunk Cable: 875 P3
Primary Feeder Cable: 875 P3 or 625 P3""",
#north texas
          "north texas dallas coax equipment":
"""Tap Manufacturer: Regal (Common) – Use in Dallas Proper
Available Tap Values:
Antronix - Do not use 26 or higher taps
Coupler Manufacturer: Regal/GI (Common) – Use in Dallas Proper
Coupler Models: Common – SSP-3, SSP-7K, SSP-9K, SSP-12K
Multi Split Manufacturer: Regal (Common) – Use in Dallas Proper
Multi Split Models: Common – SSP-3-636K

Mesquite and Richardson:
Antronix

Actives:
New Node (Outside) NC4000 @48, NC4000 @51
New Node (Inside) NC2000 @48, NC2000 @51
New Amp (outside) BTD-1000 @51, BTD-1000 @48
MB-1000 @51, MB-1000 @48
BLE-1000 @51, BLE-1000 @48
New Plug-In BLE-1000 @48
""",
          "north texas dallas power supply info":
"""Power Supply Model: AL_XM3_18_90_2_SB
Power Supply Max Load: 80% or 14.4a out of 18 
Status monitoring: All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.
The tap will be designed like a normal tap and should never be placed in trunk. If there is an existing tap within standard drop distance from the PS with an open port, then a port from that tap can be used as a Status Monitor. """,
          "north texas dallas naming standards":
""" Node:
Hub + Node
Example: 25H1

Active naming: 
hub + node + bus leg + cascade # + unique branch (letter) + unique branch(#)

Segmented node-actives:
hub + node + segment + bus leg + cascade (#) + unique branch (letter) + unique branch (#)
""",
          "north texas dallas wifi designs":
"""The Wifi devices are mounted on poles, strand or buildings and will be fed by a specialized power passing tap with a cable simulators or EQ value. The Wifi devices (Access Points – APs) are represented on the map by the WifiAP cell type from the COAXMISCCELL feature from the Command Manager.
Taps are placed at each Wifi location and a drop is run from the tap to the device. The taps are 2-port types only. One port is configured for power, but one tap can still feed two Wifi devices if needed. The power passing tap minimum outputs is 5dB on the forward. The return specification is 40dB. The Wifi device can work from 9dB to -15dB per specifications. If the tap and Wifi device are not located on the same pole/location, Wifi-specific drops are available depending on the drop distance:
1. WiFi
2. WiFi_100 – 100’
3. WiFi_225 – 225’
4. WiFi_350 – 350’
Wifi How-To:
1. Power passing tap will be inserted into the design at each location noted from field. First location is noted as AP-1
2. Placing power passing tap
o Delete device/cable before or after where the tap is going to be.
o Before drafting the design, update tap manufacturer to ANT_WIFI. Bentley Comms will now place a tap according to the Wifi design specs.
o Start design from previous cable or device
o Choose cable and drop type
o Type in “0” since there is no house count associated to this tap, and then select the pole. A new power passing tap will be placed.
o Replace the device or cable deleted previously and reconnect devices/cable downstream and Recalc
o Place Wifi cell with COAXMISCCELL wherever it is located (pole/strand/building)
o Place Wifi AP name with COAXMISCTEXT
AP[NODENAME][AP NUMBER]P""",
          #el paso
          #"north texas el paso cables":
                     "el paso cables":
          """Cables:
          Primary Trunk Cable: 875 P3
          Primary Feeder Cable: 625 P3
                    """,
                    "el paso equipment":
          """
          Available Taps: 
          ANTRNX 4-23
          Coupler Manufacturer: 
          Varies
          Coupler Models:
          1. External - 2Way = MGLS2 DC8 = MGDC2108 DC12 = MGDC2112
          2. Internal - 2Way = SS-1000-2 DC8 = SDC-1000-8 DC12 = SDC-1000-12
          Multi Split Manufacturer:
          Varies
          Multi Split Models: 
          3Way = MGLS3

          Note: 26/29 taps will not be placed during new design

          Notes: All actives and taps that are added or modify must be 1GHz equipment as per James Tucker. All new nodes will be 1GHz / Node + 1 (Node and one active in cascade) the active can be Type 2 Term BR, Type 2 LE, or C-Cor Therm LE. Also need to equally balance the passings on all legs as best as possible. Total passing’s for a new node is 250able Types

          Cascade: 
          new; is N+1
          existing;  Existing Legacy Areas is N+2 Amps +3 LE’s (Dual LE’s OK to use as an LE)
                    """,
                    "el paso power supply info":
          """Power info:
          Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18

          Status monitoring:
          All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.
          The tap will be designed like a normal tap and should never be placed in trunk. If there is an existing tap within standard drop distance from the PS with an open port, then a port from that tap can be used as a Status Monitor.
          """,
                    "el paso naming standards":
          """Power supply naming:
          node name + alpha letter
          i.e. E604A

          node naming: 
          i.e. E226
          hub + node

          segmented node  naming:
          i.e E226A
          HUB + node + segment(letter)

          Active naming:
          i.e. E2265C0
          HUB + NODE SEQUENTIAL + AMP + LEG OF AMP + LE IN CASCADE

          segmented active naming:
          E226A5C0
          HUB + NODE + SEGMENT + AMP + LEG OF AMP + LE IN CASCADE
          """,
                    "el paso wifi designs":"No Wifi designs in this project",


          #north texas witchita falls
                    #"north texas witchita falls cables":
                     "witchita falls cables":
          """Cables:
          Primary Trunk Cable: .875 P3
          Primary Feeder Cable: .625 P3""",
                    "north texas witchita falls coax equipment":
          """Available Taps: Antronix
          2 thru 23 (Do not use 26 or higher value taps)
          Coupler Manufacturer: Varies
          Coupler Models:
          1. External – 2 Way = AN_LS2, AN_DC08, AN_DC12, AN_DC16
          2. Internal – 2 Way = MO_MB-SP, MO_MB-DC8/10/12
          Multi Split Manufacturer: Antronix
          Multi Split Models: AN_LS3

          Active Models:
          1. NODES
          o AR_OM4100_4_1X4_45
          o AR_OM4100_2X2_45
          o AR_OM4100_4X4_45
          2.TRUNK
          o FNT 700 TYPE1H (3 Output)
          o CC_FNT700_3_MB_44
          o CC_FNT700_3_MB_41
          o CC_FNT700_3_MB_39
          3. FNB 700 TYPE2H (2 Output)
          o CC_FNB700_2_MB_44
          o CC_FNB700_2_MB_41
          o CC_FNB700_2_MB_39

          1.LE
          o E72 THERMAL & AGC
          o CC_E72CJ_1_A_41
          o CC_E72CJ_1_A_39
          o CC_E71CJ_1_TA_37
          o CC_E70CJ_1_TA_27
          X E72 THERMAL & AGC
          o CC_E72CJ_1_T_44
          o CC_E72CJ_1_T_41
          o CC_E72CJ_1_T_39

          note: New Nodes in a greenfield environment for MDU's, MTU's and Subdivisions will limit the cascading of amplifiers for an HFC Architecture plant to Node +2""",
                    "north texas witchita falls supply info":
          """Power info:
          Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18

          status monitoring: All new supplies will be installed with status monitoring equipment. To provide a signal path back to the headend for the SM module, a tap must be designed at all new supply locations.""",
                    "north texas witchita falls naming standards":
          """Node naming:
          Example: 6016
          hub + node

          segmented node naming:
          hub + node + segment(letter)


          active naming:
          hub + node + trunk amp + line extender


          segmented active naming:
          hub + node + segment(letter) + trunk amp(number) + line extender(letter)
          """,
          #north texas ends here
          #south-texas-san-antonio starts here
          "south texas san antonio":"""Search for the city 
          instead, such as Santonio, kerrville, cuero, eagle lake, fredericksburg""",


          #cuero 

                    "Cuero coax cables":
          """Cables:
          Primary Trunk Cable: .875 P3
          Primary Feeder Cable: .625 P3, .875 P3""",
                    "Cuero coax equipment":
          """Taps:
          Milennium / 4-23

          Coupler: Antronix / Regal / SA

          Coupler models:
          2-Way: MGLS2 / RLS10-2 / SAS2MM / DC-8: MGDC2108 / RLD10-8 / SADC8MM / DC-12: MGDC2112 / RLD10-12 SADC12MM
          Multi-split models:
          MGLS3 / RLS10-3 / RLS10-3B / SAS3UMM

          Trunk:
          870 UBT / 870 HGBT / 870 HGD / 870 TRUNK
          LE's:
          870 LE / 870 HGDLE

          Note:
          1. Amps @ trunk levels = unbalanced triples or Type 4A 2. Terminating Bridger = balanced triples or high gain dual LE’s = Type 3A or high gain duals LE’s 
          3.1 cascade = Bridger level LE’s 
          4. 2 or 3 cascade = derated by 3dB High gain duals used as Line Extenders
          1. Low density: N+7: 4 Trunk, 1 Bridger, 3 LEs 
          2. High density: N+6: 2 Trunks,""",
                    "Cuero power supply info":
          """Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18""",
                    "Cuero  naming standards":
          """Power naming:
          Node Name, followed by a letter starting with "A", and named sequentially throughout the node.

          san antonio active naming:

          Example: 1476
          hub + node

          san antonio active naming:

          hub + node + power supply (letter) + node leg(#) + amp (letter) + le (letter) + return xmitter(letter) + node type (i.e. 2)

          Other market node naming:
          Example: AH122A100
          hub + node 

          other market active naming:
          [Hub][Node Name][Power Supply Name][Amp][Leg of Amp][LE in Cascade]""",
                    "Cuero wifi designs":"""The Wifi devices are mounted on poles, strand or buildings and will be fed by a specialized power passing tap with a cable simulators or EQ value. The Wifi devices (Access Points – APs) are represented on the map by the WifiAP cell type from the COAXMISCCELL feature from the Command Manager.
          Taps are placed at each Wifi location and a drop is run from the tap to the device. The taps are 2-port types only. One port is configured for power, but one tap can still feed two Wifi devices if needed. The power passing tap minimum outputs is 5dB on the forward. The return specification is 40dB. The Wifi device can work from 9dB to -15dB per specifications. If the tap and Wifi device are not located on the same pole/location, Wifi-specific drops are available depending on the drop distance:
          1 WiFi
          2. WiFi_100 – 100’
          3.WiFi_225 – 225’
          4. WiFi_350 – 350’
          Wifi How-To:
           Power passing tap will be inserted into the design at each location noted from field. First location is noted as AP-1
           Placing power passing tap
          o Delete device/cable before or after where the tap is going to be.
          o Before drafting the design, update tap manufacturer to ANT_WIFI. Bentley Comms will now place a tap according to the Wifi design specs.
          o Start design from previous cable or device
          o Choose cable and drop type
          o Type in “0” since there is no house count associated to this tap, and then select the pole. A new power passing tap will be placed.
          o Replace the device or cable deleted previously and reconnect devices/cable downstream and Recalc
          o Place Wifi cell with COAXMISCCELL wherever it is located (pole/strand/building)
          o Place Wifi AP name with COAXMISCTEXT
           AP[Nodename][AP number]P""",

          #eagle lake

             "eagle lake coax cables":
          """Cables:
          Primary Trunk Cable: .875 P3
          Primary Feeder Cable: .625 P3, .875 P3""",
                    "eagle lake coax equipment":
          """Taps:
          Milennium / 4-23

          Coupler: Antronix / Regal / SA

          Coupler models:
          2-Way: MGLS2 / RLS10-2 / SAS2MM / DC-8: MGDC2108 / RLD10-8 / SADC8MM / DC-12: MGDC2112 / RLD10-12 SADC12MM
          Multi-split models:
          MGLS3 / RLS10-3 / RLS10-3B / SAS3UMM

          Trunk:
          870 UBT / 870 HGBT / 870 HGD / 870 TRUNK
          LE's:
          870 LE / 870 HGDLE

          Note:
          1. Amps @ trunk levels = unbalanced triples or Type 4A 2. Terminating Bridger = balanced triples or high gain dual LE’s = Type 3A or high gain duals LE’s 
          3.1 cascade = Bridger level LE’s 
          4. 2 or 3 cascade = derated by 3dB High gain duals used as Line Extenders
          1. Low density: N+7: 4 Trunk, 1 Bridger, 3 LEs 
          2. High density: N+6: 2 Trunks,""",
                    "eagle lake power supply info":
          """Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18""",
                    "eagle lake naming standards":
          """Power naming:
          Node Name, followed by a letter starting with "A", and named sequentially throughout the node.

          san antonio active naming:

          Example: 1476
          hub + node

          san antonio active naming:

          hub + node + power supply (letter) + node leg(#) + amp (letter) + le (letter) + return xmitter(letter) + node type (i.e. 2)

          Other market node naming:
          Example: AH122A100
          hub + node 

          other market active naming:
          [Hub][Node Name][Power Supply Name][Amp][Leg of Amp][LE in Cascade]""",
                    "eagle lake  wifi designs":"""The Wifi devices are mounted on poles, strand or buildings and will be fed by a specialized power passing tap with a cable simulators or EQ value. The Wifi devices (Access Points – APs) are represented on the map by the WifiAP cell type from the COAXMISCCELL feature from the Command Manager.
          Taps are placed at each Wifi location and a drop is run from the tap to the device. The taps are 2-port types only. One port is configured for power, but one tap can still feed two Wifi devices if needed. The power passing tap minimum outputs is 5dB on the forward. The return specification is 40dB. The Wifi device can work from 9dB to -15dB per specifications. If the tap and Wifi device are not located on the same pole/location, Wifi-specific drops are available depending on the drop distance:
          1 WiFi
          2. WiFi_100 – 100’
          3.WiFi_225 – 225’
          4. WiFi_350 – 350’
          Wifi How-To:
           Power passing tap will be inserted into the design at each location noted from field. First location is noted as AP-1
           Placing power passing tap
          o Delete device/cable before or after where the tap is going to be.
          o Before drafting the design, update tap manufacturer to ANT_WIFI. Bentley Comms will now place a tap according to the Wifi design specs.
          o Start design from previous cable or device
          o Choose cable and drop type
          o Type in “0” since there is no house count associated to this tap, and then select the pole. A new power passing tap will be placed.
          o Replace the device or cable deleted previously and reconnect devices/cable downstream and Recalc
          o Place Wifi cell with COAXMISCCELL wherever it is located (pole/strand/building)
          o Place Wifi AP name with COAXMISCTEXT
           AP[Nodename][AP number]P""",


          #fredericksburg
             "fredericksburg coax cables":
          """Cables:
          Primary Trunk Cable: .875 P3
          Primary Feeder Cable: .625 P3, .875 P3""",
                    "fredericksburg nevada coax equipment":
          """Tap: 
          Milennium 4-23

          Coupler MFG:
          Regal
          RLS10-2 / RLDC10-8 / RLDC10-12

          Multisplit model:
          Regal
          RLS10-3

          Trunk: 
          870 UBT /  870 HGBT / 870 HGD / 870 TRUNK

          LE's
          870 LE / 870 HGDLE

          Note:
          1.LE - Total Cascade 1: ACI LX1 MAN or ACI HI LE LE  2. Total Cascade 3: ACI LX1 MAN then ACI LX2 AGC then ACI LX3 MAN
          1. N+6 2-Trk Amps 1-Bridger 3-Le's""",
                    "fredericksburg power supply info":
          """Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18""",
                    "fredericksburg nevada naming standards":
          """Power naming:
          Node Name, followed by a letter starting with "A", and named sequentially throughout the node.

          san antonio active naming:

          Example: 1476
          hub + node

          san antonio active naming:

          hub + node + power supply (letter) + node leg(#) + amp (letter) + le (letter) + return xmitter(letter) + node type (i.e. 2)

          Other market node naming:
          Example: AH122A100
          hub + node 

          other market active naming:
          [Hub][Node Name][Power Supply Name][Amp][Leg of Amp][LE in Cascade]""",
                    "fredericksburg wifi designs":
          """The Wifi devices are mounted on poles, strand or buildings and will be fed by a specialized power passing tap with a cable simulators or EQ value. The Wifi devices (Access Points – APs) are represented on the map by the WifiAP cell type from the COAXMISCCELL feature from the Command Manager.
          Taps are placed at each Wifi location and a drop is run from the tap to the device. The taps are 2-port types only. One port is configured for power, but one tap can still feed two Wifi devices if needed. The power passing tap minimum outputs is 5dB on the forward. The return specification is 40dB. The Wifi device can work from 9dB to -15dB per specifications. If the tap and Wifi device are not located on the same pole/location, Wifi-specific drops are available depending on the drop distance:
          1 WiFi
          2. WiFi_100 – 100’
          3.WiFi_225 – 225’
          4. WiFi_350 – 350’
          Wifi How-To:
           Power passing tap will be inserted into the design at each location noted from field. First location is noted as AP-1
           Placing power passing tap
          o Delete device/cable before or after where the tap is going to be.
          o Before drafting the design, update tap manufacturer to ANT_WIFI. Bentley Comms will now place a tap according to the Wifi design specs.
          o Start design from previous cable or device
          o Choose cable and drop type
          o Type in “0” since there is no house count associated to this tap, and then select the pole. A new power passing tap will be placed.
          o Replace the device or cable deleted previously and reconnect devices/cable downstream and Recalc
          o Place Wifi cell with COAXMISCCELL wherever it is located (pole/strand/building)
          o Place Wifi AP name with COAXMISCTEXT
           AP[Nodename][AP number]P""",

          #San Antonio
             "san antonio coax cables":
          """Cables:
          Primary Trunk Cable: .875 P3
          Primary Feeder Cable: .625 P3, .875 P3""",
                    "san antonio coax equipment":
          """Multi split models: RS10-3

          Coupler models:
          RLS10-2 
          RLDC10-8 
          RLDC10-12

          SATX1G_N1 Trunk:
          FMB901e
          FM901e
          SATX750 Trunk:FNT72 TB FNB75 TMB


          Note(SATX750):
          1. A=AGC Use on 2nd LE in 3 Cascade M=Manual - Use on UG T=Thermal - Use on Aerial
          2. N+6 2-Trk Amps 1-Bridger 3-Le's
          Note(SATX1G_N1):
          1. N+1
          SATX750 LE's:
          E72CJ TLC / E72CJ / ALC / E72CJ MAN
          SATX1G_N1 LE's:
          FM331
          note: All equipment here is regal, unless stated otherwise.
          Notes: Do not use 26 or higher value taps""",
                    "san antonio power supply info":
          """Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18""",
                    "san antonio naming standards":
          """Power naming:
          Node Name, followed by a letter starting with "A", and named sequentially throughout the node.

          san antonio active naming:

          Example: 1476
          hub + node

          san antonio active naming:

          hub + node + power supply (letter) + node leg(#) + amp (letter) + le (letter) + return xmitter(letter) + node type (i.e. 2)

          Other market node naming:
          Example: AH122A100
          hub + node 

          other market active naming:
          [Hub][Node Name][Power Supply Name][Amp][Leg of Amp][LE in Cascade]""",
                    "san antonio wifi designs":"""The Wifi devices are mounted on poles, strand or buildings and will be fed by a specialized power passing tap with a cable simulators or EQ value. The Wifi devices (Access Points – APs) are represented on the map by the WifiAP cell type from the COAXMISCCELL feature from the Command Manager.
          Taps are placed at each Wifi location and a drop is run from the tap to the device. The taps are 2-port types only. One port is configured for power, but one tap can still feed two Wifi devices if needed. The power passing tap minimum outputs is 5dB on the forward. The return specification is 40dB. The Wifi device can work from 9dB to -15dB per specifications. If the tap and Wifi device are not located on the same pole/location, Wifi-specific drops are available depending on the drop distance:
          1 WiFi
          2. WiFi_100 – 100’
          3.WiFi_225 – 225’
          4. WiFi_350 – 350’
          Wifi How-To:
           Power passing tap will be inserted into the design at each location noted from field. First location is noted as AP-1
           Placing power passing tap
          o Delete device/cable before or after where the tap is going to be.
          o Before drafting the design, update tap manufacturer to ANT_WIFI. Bentley Comms will now place a tap according to the Wifi design specs.
          o Start design from previous cable or device
          o Choose cable and drop type
          o Type in “0” since there is no house count associated to this tap, and then select the pole. A new power passing tap will be placed.
          o Replace the device or cable deleted previously and reconnect devices/cable downstream and Recalc
          o Place Wifi cell with COAXMISCCELL wherever it is located (pole/strand/building)
          o Place Wifi AP name with COAXMISCTEXT
           AP[Nodename][AP number]P""",


      
          #kerrville
             "Kerrville coax cables":
          """Cables:
          Primary Trunk Cable: .875 P3
          Primary Feeder Cable: .625 P3, .875 P3""",
                    "Kerrville  nevada coax equipment":
          """Taps:
          Milennium / 4-23

          Coupler: Antronix / Regal / SA

          Coupler models:
          2-Way: MGLS2 / RLS10-2 / SAS2MM / DC-8: MGDC2108 / RLD10-8 / SADC8MM / DC-12: MGDC2112 / RLD10-12 SADC12MM
          Multi-split models:
          MGLS3 / RLS10-3 / RLS10-3B / SAS3UMM

          Trunk:
          870 UBT / 870 HGBT / 870 HGD / 870 TRUNK
          LE's:
          870 LE / 870 HGDLE

          Note:
          1. Amps @ trunk levels = unbalanced triples or Type 4A 2. Terminating Bridger = balanced triples or high gain dual LE’s = Type 3A or high gain duals LE’s 
          3.1 cascade = Bridger level LE’s 
          4. 2 or 3 cascade = derated by 3dB High gain duals used as Line Extenders
          1. Low density: N+7: 4 Trunk, 1 Bridger, 3 LEs 
          2. High density: N+6: 2 Trunks,""",
                    "Kerrville  nevada power supply info":
          """Power Supply Model: AL_XM3_18_90_2_SB
          Power Supply Max Load: 80% or 14.4a out of 18""",
                    "Kerrville nevada naming standards":
          """Power naming:
          Node Name, followed by a letter starting with "A", and named sequentially throughout the node.

          san antonio active naming:

          Example: 1476
          hub + node

          san antonio active naming:

          hub + node + power supply (letter) + node leg(#) + amp (letter) + le (letter) + return xmitter(letter) + node type (i.e. 2)

          Other market node naming:
          Example: AH122A100
          hub + node 

          other market active naming:
          [Hub][Node Name][Power Supply Name][Amp][Leg of Amp][LE in Cascade]""",
                    "Kerrville  nevada  wifi designs":"""The Wifi devices are mounted on poles, strand or buildings and will be fed by a specialized power passing tap with a cable simulators or EQ value. The Wifi devices (Access Points – APs) are represented on the map by the WifiAP cell type from the COAXMISCCELL feature from the Command Manager.
          Taps are placed at each Wifi location and a drop is run from the tap to the device. The taps are 2-port types only. One port is configured for power, but one tap can still feed two Wifi devices if needed. The power passing tap minimum outputs is 5dB on the forward. The return specification is 40dB. The Wifi device can work from 9dB to -15dB per specifications. If the tap and Wifi device are not located on the same pole/location, Wifi-specific drops are available depending on the drop distance:
          1 WiFi
          2. WiFi_100 – 100’
          3.WiFi_225 – 225’
          4. WiFi_350 – 350’
          Wifi How-To:
           Power passing tap will be inserted into the design at each location noted from field. First location is noted as AP-1
           Placing power passing tap
          o Delete device/cable before or after where the tap is going to be.
          o Before drafting the design, update tap manufacturer to ANT_WIFI. Bentley Comms will now place a tap according to the Wifi design specs.
          o Start design from previous cable or device
          o Choose cable and drop type
          o Type in “0” since there is no house count associated to this tap, and then select the pole. A new power passing tap will be placed.
          o Replace the device or cable deleted previously and reconnect devices/cable downstream and Recalc
          o Place Wifi cell with COAXMISCCELL wherever it is located (pole/strand/building)
          o Place Wifi AP name with COAXMISCTEXT
           AP[Nodename][AP number]P""",
           "sierra nevada coax cables":
      """Cables:
      Primary Trunk Cable: 875 Aerial; 875 Underground
      Primary Feeder Cable: 625 Aerial; 625 Underground""",
                "sierra nevada coax equipment":
      """ Taps: SA
      32/23 & 29/23 & 26/23 window taps; 23 to 8 & 4 two port
      Coupler Manufacturer: SA
      Coupler Models: SA SG 2,3,8,12,16,PI
      Multi Split Manufacturer: SA & Motorola
      Multi Split Models: Multi out, Int 2-way, Int DC-8, Int DC-12

      actives: SA gainmaker 1GHZ; Motorola 1GHZ""",
                "sierra nevada power supply info":
      """Power info:
      Power Supply Model: AL_XM3_18_90_2_SB
      Power Supply Max Load: 80% or 14.4a out of 18

      Status monitoring:
      Status monitoring from tap port not more than 150’ from PS drafted with P-STMON block on the P- power layer.""",
                "sierra nevada naming standards":
      """Node naming:
      first 2 characters of Headend + 3 digit sequential number + (i.e. Coos Bay = CB001). The series can be
      note: (i.e. CB200 can represent Florence, OR which is fed from the Coos Bay Headend.)

      Active naming:
      Amplifiers shall be named with 2 digits that represent the amplifier’s number. (i.e. 01 thru 99) When drafted, this number will be combined with the node number to display as CB20099 in the amplifier ID block. The node will always be the first named active (i.e. CB10201).
      """,
                "sierra nevada wifi designs":"Not done in this area",
          #south texas ends here
          #texas regions end here
          #carolina regions begin here
            "western north carolina cables": 
"""Primary Trunk Cable: 875P3
Primary Feeder Cable: 625P3""",
          
            "western north carolina coax equipment":
"""Tap Manufacturer: Antronix
Available Tap Values: 4-24
Coupler Manufacturer: Varies
Coupler Models: 2Way, DC8, DC12
Multi Split Manufacturer: Varies
Multi Split Models: TRKUN3 & FEDUN3
note: 17v and over taps must be four ports. 
note: For actives On new node designs, SW_MTA750 will be used for all areas.
Nodes: OPTIMAX3100
Amplifiers: FLEX MAX901e BDG
Line Extenders: FLEX MAX901e, FM331-T, FM331-A

[Cascade Limit: All 870 MHz design areas are N+6. All 1 GHz design is N+2 max.
Existing Design: Max Cascade is N+6 in all markets (enterprise) – you can add any plant to an existing node as long as you don’t break that hard-coded rule of cascade…
That said – if you’re adding greater than a commercial/tni order to an existing node, we need to check]""",

          "western north carolina power supply info":
          """AL_XM3_18_90_2_SB
Power Supply Max Load: 80% or 14.4a out of 18""",
"Western north carolina POWER SUPPLY NAMING":
"""Power Supply:The power supply takes on the node boundary names that it is located. The first supply will be the A supply.

STATUS MONITORING: Status monitoring, a tap will locate within 200’ of the supply. New design will place a tap at the PS location, or run signal back on the power jumper and place the inserter at the PS.

NODE NAMING: Node Naming i.e. BR104
BR 104
Hub Node #

ACTIVE NAMING: [hub(BR)] + [node(104)] + [trunk active(01)]  + [feeder active(A)]""",
          #Wisconsin
          "wisconsin cables":
"""Cables:
Primary Trunk Cable: P3.875
Primary Feeder Cable: P3.625
          """,
          "wisconsin coax equipment":
"""Passives:
Tap Manufacturer: GI P Series (FFT P)
GI N Series (FFT N)
Regal 1GHz (Standard RMT1)
SA 1GHz (SAT G)
SA MultiMedia (SAT MM)
Available Tap Values: 8 to 23

Coupler Manufacturer: 
Regal 1GHz (RL)
SA 1GHz (SA G)
SA MultiMedia (SA MM)
SA Surge-Gap (SA SG)
GI N Series (SSP N)
Coupler Models: 2-Way, DC-8, DC-12, and DC-16 for all manufacturers except GI.
GI : 2-Way, DC-7, DC-9, DC-12, and DC-16.

Active models:
Node: 
Aurora NC4000
Amplifiers:
MB100S-2HAXH-F Scientific Atlanta: GainMaker High Gain Dual System Amplifier 1GHz
Line Extenders:
BLE100 1GHz Line Extender Scientific Atlanta: GainMaker Line Extender 1GHz


Multi Split Manufacturer Multi Split Models:
Regal 1GHz  || RLS10-3-12A
SA 1GHz ||  SA3-WAY G
SA MultiMedia || SAS3UMM
SA Surge-Gap || SA SG 3-WAY U
GI N Series || SSP-3-636N
          """,
          "wisconsin power supply info":
"""2.1 Power Supply Info
Power Supply Model: AL_XM3_18_90_2_SB
Power Supply Max Load: 80% or 14.4a out of 18

Status Monitoring:
Indicated by symbol on map S/M. Refer to the existing drafting on the map and compare it to the Lode file to determine if status monitoring is necessary in that city. This will also indicate whether to use an unused tap port or a DC-16 coupler for the status monitor.
          """,
          "wisconsin naming standards":
"""Active Naming:
Actives will usually be named a 2 digit number, and the node itself will usually be active 01.
Power Supply Naming
Number is associated to each node sequentially use A, B, C, D, E etc. Generally, Power Supply A will feed the node.

Node Naming:
Most node names are a single digit indicating the region code, followed by two letters indicating the city, followed by a two digit number indicating the node number. Example Lode file name: 5JA01 for node 1 in Janesville.
Some node names are a two digit number indicating the region code, followed by a letter indicating the city, followed by a two digit""",
          "wisconsin wifi designs":"Not done in this area.",   
      }

    def get_state_info(self, state_name):
        state_name = state_name.lower()
        return self.state_info.get(state_name, "State information not found.")



class RegionGenerator:
    def __init__(self):
        self.regions = {
            "Georgia": "CHFIBER",  # GEORGIA
            "georgia": "CHFIBER",
            "GEORGIA": "CHFIBER",
            "Alabama": "Birmingham",  # Alabama
            "alabama": "Birmingham",
            "ALABAMA": "Birmingham",
            "Alexander city": "TWCAL",
            "alexander city": "TWCAL",
            "ALEXANDER CITY": "TWCAL",
            "AUBURN, AL":"TWCAL",
            "auburn, al":"TWCAL",
            "AUBURN, ALABAMA":"TWCAL",
            "auburn, alabama":"TWCAL",
            "leeds": "TWCAL",
            "LEEDS": "TWCAL",
            "Leeds": "TWCAL",
            "California": "LAMETRO",  # CALIFORNIA
            "california": "LAMETRO",
            "CALIFORNIA": "LAMETRO",
            "AMITE, LA": "TWGTTX",
            "PASO ROBLES, CA": "SCALENT",
            "paso robles, california":"SCALENT",
            "paso robles, CA":"SCALENT",
            "PASO ROBLES, CALIFORNIA":"SCALENT",   
            "Colorado": "TWCO",  # COLORADO
            "colorado": "TWCO",
            "COLORADO": "TWCO",
            "Connecticut": "TWMAINE",  # CONNECTICUT
            "CONNECTICUT": "TWMAINE",
            "connecticut": "TWMAINE",
            "IDAHO":"TWNW",  #IDAHO
            "idaho":"TWNW",
            "POST FALLS, ID":"TWNW",
            "post falls, id":"TWNW",
            "POST FALLS, IDAHO":"TWNW",
            "post falls, idaho":"TWNW",
            "Delaware": "TWDEL",  # INDIANA
            "EVANSVILLE, INDIANA":"TWKIWI",
            "evansville, indiana":"TWKIWI",
            "Evansville, Indiana":"TWKIWI",
            "evansville, IN":"TWKIWI",
            "ILLINOIS": "CFHBIER",  # Illinois
            "Illinois": "CFHBIER",
            "illinois": "CFHBIER",
            "Slidell": "birmingham",  # Louisiana
            "slidell": "birmingham",
            "SLIDELL": "birmingham",
            "LOUISIANA": "CHFIBER",
            "Louisiana": "CHFIBER",
            "louisiana": "CHFIBER",
            "Maryland": "TWCVA",  # maryland
            "MARYLAND": "TWCVA",
            "maryland": "TWCVA",
            "Massachusetts": "TWMAINE",  # massachusetts
            "MASSACHUSETTS": "TWMAINE",
            "massachusetts": "TWMAINE",
            "Michigan": "DETROIT",  # Michigan
            "michigan": "DETROIT",
            "MICHIGAN": "DETROIT",
            "lanse, mi":"CHFIBER",
            "LANSE, MI":"CHFIBER",
            "LANSE, MICHIGAN":"CHFIBER",
            "lanse, michigan":"CHFIBER",
            "A":"CHFIBER",
            "Minnesota": "CHFiber",  #MINNESOTA
            "minnesota": "CHFiber",
            "MINNESOTA": "CHFiber",
            "Mississippi": "BIRMINGHAM",  # Mississippi
            "mississippi": "BIRMINGHAM",
            "MISSISSIPPI": "BIRMINGHAM",
            "MONTANA": "CHFIBER",  # Montana
            "Montana": "CHFIBER",
            "montana": "CHFIBER",
            "NEBRASKA": "TWLIN",  # NEBRASKA
            "Nebraska": "TWLIN",
            "nebraska": "TWLIN",
            "carson city": "LAMETRO",  # Nevada
            "Carson city": "LAMETRO",
            "CARSON CITY": "LAMETRO",
            "nevada": "CHFIBER",
            "Nevada": "CHFIBER",
            "NAVADA": "CHFIBER",
            "New york": "TWSYRA",  # New York
            "New York": "TWSYRA",
            "NEW YORK": "TWSYRA",
            "new york": "TWSYRA",
            "North Carolina": "TWRAL",  # NORTH CAROLINA
            "north Carolina": "TWRAL",
            "North carolina": "TWRAL",
            "north carolina": "TWRAL",
            "NORTH CAROLINA": "TWRAL",
            "ASHEVILLE, NC":"TWCLT",
            "ASHEVILLE, NORTH CAROLINA":"TWCLT",
            "asheville, nc":"TWCLT",
            "asheville, north carolina":"TWCLT",  
            "North Wilkesboro": "TWGBO",
            "Lenoir": "TWCLT",
            "Boone": "TWCLT",
            "OHIO":"TWSOH",      #OHIO
            "WARREN, OHIO" : "TWSOH",
            "warren, ohio" : "TWSOH",
            "warren, oh" : "TWSOH",
            "WARREN, OH": "TWSOH",
            "TWSOH1": "TWSOH",
            "TWSOH":"TWSOH",
            "VINCENT, OH":"TWCOLU",
            "VINCENT, OHIO":"TWCOLU",
            "vincent, oh":"TWCOLU",
            "vincent, ohio":"TWCOLU",
            "COLUMBUS, OH":"TWCOLU",
            "COLUMBUS, OHIO":"TWCOLU",
            "columbus, oh":"TWCOLU",
            "columbus, ohio":"TWCOLU",
            "OREGON": "TWWAID",  # Oregon
            "oregon": "TWWAID",
            "Oregon": "TWWAID",
            "Bookings": "TWWAID",
            "tennesee": "TWKIWI",  # TENNESSEE
            "Tennesee": "TWKIWI",
            "TENNESEE": "TWKIWI",
            "MCMINNVILLE, TN":"BIRMINGHAM",
            "mcminnville, tn":"BIRMINGHAM",
            "Mcminnville, TN":"BIRMINGHAM",
            "mcminnvile, tennesee":"BIRMINGHAM",
            "texas": "TWNTX",  # TEXAS
            "Texas": "TWNTX",
            "TEXAS": "TWNTX",
            "VERMONT": "TWMAINE",  # VERMONT
            "Vermont": "TWMAINE",
            "vermont": "TWMAINE",
            "virginia": "TWCVA",  # virginia
            "VIRGINIA": "TWCVA",
            "Virginia": "TWCVA",
            "WASHINGTON": "TWWAID",  # Washington
            "Washington": "TWWAID",
            "washington": "TWWAID",
            "Wisconsin": "TWWISC",
            "wisconsin": "TWWISC",
            "WISCONSIN": "TWWISC",
            "Wyoming": "CHFIBER",  # WYOMING
            "wyoming": "CHFIBER",
            "WYOMING": "",
            "XX": "XX1",  # BLOATERCODE
            "XXX": "XXX1",
            "XXXX": "XXXX1",
            "XZ": "XXZ1",
            "XXZ": "XXZ1",

            # Add more regions as needed
        }

    def get_region(self, region_name):
      return self.regions.get(region_name.lower(), "Region not found.")


class TestBot:
    def take_test(self, questions, options, correct_answers):
        total_questions = len(questions)
        correct_guesses = 0
        guesses = []

        print("\n--- Start Test ---")

        for i in range(total_questions):
            print(f"\nQuestion {i + 1}: {questions[i]}")
            for j in range(len(options[i])):
                print(f"{chr(65 + j)}. {options[i][j]}")

            guess = input("Enter (A, B, C, D): ").upper()
            guesses.append(guess)

            if guess == correct_answers[i].upper():
                print("CORRECT CHOICE")
                correct_guesses += 1
            else:
                print("Wrong choice")

        print("\n--- End Test ---")

        self.display_score(correct_guesses, total_questions, guesses)

    def display_score(self, correct_guesses, total_questions, guesses):
        print("\n-------------------------------------------")
        print("RESULTS")
        print("-------------------------------------------")

        print("Answers:")
        for i in range(total_questions):
            print(f"{i + 1}. {guesses[i]}")

        score = (correct_guesses / total_questions) * 100
        print(f"\nYour score is: {score:.2f}%")


#Report issue function
def report_issue():
    issue = input("Please describe the issue: ")
    with open("issues.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([issue])
    print("Issue reported successfully.")
  

#Main Function
def main():
  print("Hello, I am here to assist you!")
  test_bot = TestBot()
  email_generator = EmailGenerator()
  region_generator = RegionGenerator()
  state_information = StateInfo()
  geolocator = Geolocation()
  

  while True:
      user_input = input("Enter your command: ").lower()

      if user_input == "take d2 test":
          test_bot.take_test(d2_questions, d2_options, d2_correct_answers)

      elif user_input == "take d3 test":
          test_bot.take_test(d3_questions, d3_options, d3_correct_answers)

      elif user_input == "take fiber testing and maintenance conventional":
          test_bot.take_test(fiber_testing_questions, fiber_testing_options, fiber_testing_correct_answers)

      elif user_input == "get email":
          number = int(input("Enter the number for the email you want to get: "))
          email = email_generator.get_email(number)
          print("Email:", email)

      elif user_input in ["state info", "get state info", "state information", "info on this state"]:
          state_name = input(
              "Enter a state name + what you want info on '[Cables, Coax equipment, power supply Naming standards or WiFi Designs]':   ")
          state_info = state_information.get_state_info(state_name)
          print(state_info)

      elif user_input == "get region":
          region_name = input("Enter a region name: ")
          region = region_generator.get_region(region_name)
          print("Region:", region)
      elif user_input == "report":
          print("State the issue clearly, then add the date and time!")
          report_issue()
      elif user_input == "print address":  # Add geolocation as an option
          location_name = input("Enter an address: ")
          try:
              location = geolocator.get_location_details(location_name)
              if location is not None:
                  print("Address:", location.address)
                  print("Latitude:", location.latitude)
                  print("Longitude:", location.longitude)
              else:
                  print("Location not found.")
          except Exception as e:
              print("An error occurred:", str(e))

      elif user_input == "exit":
          print("Goodbye")
          break

      else:
          print("Invalid command. Please try again.")

if __name__ == "__main__":
  main()