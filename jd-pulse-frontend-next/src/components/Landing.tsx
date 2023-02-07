import {
  Button,
  Flex,
  Heading,
  Image,
  Stack,
  Text,
  useBreakpointValue,
  Link,
} from "@chakra-ui/react";
import React from "react";

export default function Landing() {
  return (
    <Stack minH={"100vh"} direction={{ base: "column", md: "row" }}>
      <Flex p={8} flex={1} align={"center"} justify={"center"}>
        <Stack spacing={6} w={"full"} maxW={"lg"}>
          <Heading fontSize={{ base: "3xl", md: "4xl", lg: "5xl" }}>
            <Text
              as={"span"}
              position={"relative"}
              _after={{
                content: "''",
                width: "full",
                height: useBreakpointValue({ base: "20%", md: "30%" }),
                position: "absolute",
                bottom: 1,
                left: 0,
                bg: "blue.400",
                zIndex: -1,
              }}
            >
              Land your dream job
            </Text>
            <br />{" "}
            <Text color={"blue.400"} as={"span"}>
              Prepare your resume
            </Text>{" "}
          </Heading>
          <Text fontSize={{ base: "md", lg: "lg" }} color={"gray.500"}>
            Maximize your chances of landing your dream job by incorporating
            relevant keywords from job descriptions into your resume with our
            easy-to-use Resume Keyword Extractor tool.
          </Text>
          <Stack direction={{ base: "column", md: "row" }} spacing={4}>
            <Link href={"/getKeywords"}>
              <Button
                rounded={"full"}
                bg={"blue.400"}
                color={"white"}
                _hover={{
                  bg: "blue.500",
                }}
              >
                Get Started
              </Button>
            </Link>
            <Link href={"#"}>
              <Button rounded={"full"}>How It Works</Button>
            </Link>
          </Stack>
        </Stack>
      </Flex>
      <Flex flex={1}>
        <Image
          alt={"Login Image"}
          objectFit={"cover"}
          src={"/landing-image.jpg"}
          maxH={"100vh"}
        />
      </Flex>
    </Stack>
  );
}
