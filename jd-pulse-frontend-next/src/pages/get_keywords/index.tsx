import React, { useState} from 'react';
import axios from "axios";
import {
    Textarea,
    Input,
    Stack,
    Container,
    Text,
    Button,
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
    Spinner,
    Tag,
    WrapItem,
    Center,
    Wrap
} from '@chakra-ui/react';



interface Data {
    keywords: string[];
    error?: string;
}

const GetKeywords: React.FC = () => {
    const [apiKey, setApiKey] = useState<string>('');
    const [jobDescription, setJobDescription] = useState<string>('');
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [data, setData] = useState<Data>({ keywords: ['test', 'test1']});
    const [isErrorModalOpen, setIsErrorModalOpen] = useState<boolean>(false);
    const [errorMessage, setErrorMessage] = useState<string>('');
    const [selectedKeyword, setSelectedKeyword] = useState<string | null>(null);

    const handleTagClick = (keyword: string) => {
        setSelectedKeyword(keyword);
        navigator.clipboard.writeText(keyword).then(r => console.log('copied'));
        setTimeout(() => {
            setSelectedKeyword(null);
        }, 200);
    };

    const handleClick = async () => {
        setIsLoading(true);
        try {
            const response = await axios.get('/api/get_keywords', { params: { open_api_key: apiKey, text: jobDescription }, });
            const receivedData: Data = response.data;

            if (receivedData.error) {
                setErrorMessage(receivedData.error);
                setIsErrorModalOpen(true);
            } else {
                setData(receivedData);
            }

        } catch (error) {
            // @ts-ignore
            setErrorMessage(error.message);
            setIsErrorModalOpen(true);
            console.error(error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <Container maxW='80%' paddingTop='1em' paddingBottom='1em'>
            <Stack>
                <Text fontSize='md'>Enter your OpenAI Api key here:</Text>
                <Input
                    placeholder="Enter text here"
                    value={apiKey}
                    onChange={(e) => setApiKey(e.target.value)}
                />
                <Text fontSize='md'>Enter your desirable job description:</Text>
                <Textarea
                    placeholder="Enter text here"
                    value={jobDescription}
                    onChange={(e) => setJobDescription(e.target.value)}
                />
                <Button
                    name={'get_keywords'}
                    size="md"
                    fontSize={'sm'}
                    fontWeight={600}
                    color={'white'}
                    bg={'twitter.500'}
                    _hover={{
                        bg: 'twitter.400',
                    }}
                    onClick={handleClick}
                >
                    {isLoading ? <Spinner /> : 'Get keywords'}
                </Button>
            </Stack>
            <Modal isOpen={isErrorModalOpen} onClose={() => setIsErrorModalOpen(false)}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader>Oops!</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        {errorMessage}
                    </ModalBody>
                    <ModalFooter>
                        <Button
                            fontSize={'sm'}
                            fontWeight={600}
                            color={'white'}
                            bg={'twitter.500'}
                            _hover={{
                                bg: 'twitter.400',
                            }}
                            mr={2}
                            onClick={() => setIsErrorModalOpen(false)}>
                            Close
                        </Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
            <Wrap paddingTop={'1em'} spacing='30px' justify='center'>
                {data.keywords.map(keyword => (
                    <WrapItem key={keyword}>
                        <Center>
                            <Tag
                                key={keyword}
                                size="lg"
                                onClick={() => handleTagClick(keyword)}
                                cursor="pointer"
                                textColor={'white'}
                                bg={selectedKeyword === keyword ? 'green' : 'twitter.500'}
                                _hover={{
                                    bg: 'twitter.400',
                                }}
                                _
                                >
                                    {keyword}
                            </Tag>
                        </Center>
                    </WrapItem>
                ))}
            </Wrap>


        </Container>
    );
};

export default GetKeywords;

